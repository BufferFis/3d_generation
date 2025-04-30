import torch
import numpy as np
import imageio
import os
import trimesh
from PIL import Image
from rembg import remove
from diffusers import ShapEImg2ImgPipeline, ShapEPipeline
from diffusers.utils import export_to_ply

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using {device}")

def remove_background(input_path, output_path = 'masked.png'):
	"""
	Input: Accepts the input path and can accept the output path to the masked image
	return: Image with removed background
	"""
	print("Removing the background from the image")
	
	img = Image.open(input_path).convert("RGBA")
	p_img = remove(img)
	p_img.save(output_path)
	
	return p_img.convert("RGB")

def image_to_3d(input_path, output_folder = 'output_image'):

	"""
	Input: input path and the output_folder if preferred
	Saves a .ply and a .obj file into the output folder
	"""
	
	os.makedirs(output_folder, exist_ok = True)
	masked = os.path.join(output_folder, "masked.png")
	
	p_img = remove_background(input_path, masked)

	pipeline = ShapEImg2ImgPipeline.from_pretrained("openai/shap-e-img2img", torch_dtype=torch.float16).to(device) 
	in_img = p_img.convert("RGB").resize((256, 256))
	out = pipeline(in_img, guidance_scale=12.0, num_inference_steps=100, frame_size=384, output_type="mesh")

	ply_path = os.path.join(output_folder, "output.ply")
	export_to_ply(out.images[0], ply_path)
	print(f"Saved PLY to {ply_path}")
	mesh = trimesh.load(ply_path)
	obj_path = os.path.join(output_folder, "output.obj")
	mesh.export(obj_path)
	print(f"Saved OBJ to {obj_path}")

	print(f"Image to 3d outputs saved to {output_folder}")

def text_to_3d(prompt, output_folder="output_text"):
	"""
	Input: recieves input prompt and output folder if preferred
	Stores the .ply and .obj file there
	"""
	os.makedirs(output_folder, exist_ok = True)

	pipeline = ShapEPipeline.from_pretrained("openai/shap-e", torch_dtype=torch.float16).to(device)
	print(f"Generating 3d from the prompt: {prompt}")

	out = pipeline([prompt], guidance_scale=12.0, num_inference_steps=100, frame_size=384, output_type='mesh')
	
	ply_path = os.path.join(output_folder, "output.ply")
	export_to_ply(out.images[0], ply_path)
	print(f"Saved PLY to {ply_path}")

	mesh = trimesh.load(ply_path)
	obj_path = os.path.join(output_folder, "output.obj")
	mesh.export(obj_path)
	print(f"Saved OBJ to {obj_path}")

def main():
	mode = input("Choose mode(text/image): ").strip().lower()

	if mode == "image":
		path = input("Enter your image file path: ").strip()
		image_to_3d(path)
	
	elif mode == "text":
		prompt = input("Enter the prompt: ").strip()
		text_to_3d(prompt)

	else:
		print("Invalid mode, pls select from the following")
		return

if __name__ == "__main__":
	main()

