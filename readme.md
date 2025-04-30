## Text and Image to 3d generation 

### Before running the script
- Either run on a system with a GPU and preferably a Debian based system or run in google collab
- Google collab pre run commands `!apt-get update && apt-get install -y xvfb libgl1-mesa-glx libosmesa6 libglfw3 cmake git`

- Followed by`!pip install -r requirements.txt`
-  For Ubuntu based system run the same commands without using the `!`
- Python Requirements are also specified in requirements.txt but following the `pip install` steps resolves and does the same job
---

### How to run the code
- The code will prompt you to input whether you want to generate the 3d mesh with a text or image, input that accordingly.
- If image was selected the specify the path of the image when the program prompts you for the path, if the image is in the same directory as just specify the name of the image with the extension.
- If text was selected just enter the prompt of what to generate.
- If mesh was generated using a image, a new folder named as output_image will be created, a masked.png will appear there which is the image after background removal, which is just to ensure whether the background removal works on not, a `.ply` and  `.obj` file will be created, the earlier one is there as it can store more information like color of the mesh, and then the later is there in accordance to submission guidelines
- If mesh was generated using a prompt, a new folder named as output_text will be generated and will contain the output in same format without the masked.png as here there was no need to preprocess the data.
- For rendering nothing is done but it can be viewed using online software like `https://3dviewer.net` as google collab is used by me to develop it where 3d rendering is not possible.
-  A image is provided for testing purposes.
- A example prompt can be `A toy car`

---
### Thought Process
- So for me it was the first time handling anything with images as a whole so I had to learn a lot but what I learned with my experience in NLP was that everything is available off the shelf on Hugging face, so my basic idea was to use all inbuilt libraries for the tasks I had to do, but before using reading about what they exactly do.
- I fired up every tool I had to find as many tools as possible which I can directly use with the line `from_pretrained` as it basically makes the life easy. 
- I came across OpenAI's shap-e and discovered that it can do text to 3d as well as image to 3d, and soon I was able to have a code which can generate a 3d object both from a text or a image
- I saw that preprocessing was mentioned so I came across rembg which literally just removes the background from the image by applying a mask on it, all this was very similar to how I can mask values in a transformer while training it for a NLP task, so i used that for that removing the background.
- I didnt use pyRender as it uses pyOpenGL, my roommate is a C/C++ developer and wanted me to use OpenGL once but I wanted to use pyOpenGL, and found out it doesn't work on google Collab which is my preferred development platform for any ML related task, as I dont have a very strong GPU like the t400.
- Found out new things like resizing to 256x256, changed data type to float 16 as its computationally light.
- For the fine tuning of parameters like Guidance Scale, num_inference_step and frame_size, I asked there meaning on the internet and was able to come to these values which I used as its one of the famous combos from my current knowledge.
- I saved as a `.ply` file as a export method existed, then used pymesh to convert and save a `.obj` file.
- I thought of doing "Why not both?", because everything was available in front of me directly and it felt like a insane experience.
- Also the outputs are not very very nice I think, but I have my final exams going on so this is all I could have achieved in 1 night of just being in front of my screen figuring out things, I would have loved to do more, but have to focus a bit to the academic side now.

Thank you for Downloading my assignment and reading all the way till the end and giving your valuable time to evaluate my project.

Made with love and caffeine by,
Samar Singh (aka BufferFis) 
