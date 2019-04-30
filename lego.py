from PIL import Image

def do_lego (name,N=32):
    LEGO=Image.open('files/lego.png')
    out_LEGO = LEGO.resize((N,N))
    out_LEGO.save('resized.png')
    LEGO = Image.open('resized.png')
    print('files/photos/{}'.format(name))
    image = Image.open('files/photos/{}'.format(name),'r')
    lx=LEGO.load()
    px=image.load()
    width, height= image.size
    out = image.resize((width // N, height // N))
    px2 = out.load()
    for i in range(width//N):
        for j in range(height//N):
            for k in range(N):
                for l in range(N):
                    r,g,b=px2[i,j]
                    lr,lg,lb=lx[k,l]
                    px[i*N+k,j*N+l]=((int(r*(lr/255))//1),(int(g*(lg/255))//1),(int(b*(lb/255))//1))
    region = image.crop((0,0,i*N+k,j*N+l))
    region.save('files/result/result_{}'.format(name))
    return True