import os
import replicate
import webbrowser
#cette commande doit etre executer avant chaque lancement
#export REPLICATE_API_TOKEN=[votre clef api replicate]

#nombre de generation:
n = 4

model = replicate.models.get("prompthero/openjourney")
version = model.versions.get("9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb")
os.system('cls' if os.name=='nt' else 'clear')
print("       .__ __  ")       
print("  ____ |__|  | ______   ____  ")      
print("_/ __ \|  |  |/ /  _ \ /    \ ")      
print("\  ___/|  |    <  <_> )   |  \ ")      
print(" \___  >__|__|_ \____/|___|  /")      
print("     \/        \/          \/ ")   
while(0 == 0):   
    print("")
    p = input("eikon-> ")
    if(p == "exit"):
        quit()
    print("chargement...")

    # https://replicate.com/prompthero/openjourney/versions/9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb#input
    inputs = {
        
        # Input prompt
        'prompt': p + ", 8k",

        # Width of output image. Maximum size is 1024x768 or 768x1024 because
        # of memory limits
        'width': 512,

        # Height of output image. Maximum size is 1024x768 or 768x1024 because
        # of memory limits
        'height': 512,

        # Number of images to output
        'num_outputs': 1,

        # Number of denoising steps
        # Range: 1 to 500
        'num_inference_steps': 50,

        # Scale for classifier-free guidance
        # Range: 1 to 20
        'guidance_scale': 6,

        # Random seed. Leave blank to randomize the seed
        # 'seed': ...,
    }

    # https://replicate.com/prompthero/openjourney/versions/9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb#output-schema
    for i in range(0,n):
        output = version.predict(**inputs)
        print("chargement fini")
        print(output)
        
