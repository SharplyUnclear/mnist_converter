# mnist converter

from pathlib import Path

def generate(img_file, label_file, txt_file, n_images):
    lbl_f = open(label_file, "rb")  # labels file
    img_f = open(img_file, "rb")  # pixels file
    txt_f = open(txt_file, "w")  # file to write to

    img_f.read(16)  # discard header info
    lbl_f.read(8)  # discard header info

    for i in range(n_images):  # number images requested
        lbl = ord(lbl_f.read(1))  # get label (unicode, one byte)
        vector = [0] * 10  # [0,0,0,0,0,0,0,0,0,0]
        vector[lbl] = 1  # [0,0,0,0,0,0,0,1,0,0]
        txt_f.write("|digit   txt_f.write(" ".join(str(x) for x in vector)")
        txt_f.write(" |pixels ")
        for j in range(784):  # get 784 pixel vals
            val = ord(img_f.read(1))
            txt_f.write(str(val) + " ")  # trailing space OK
        txt_f.write("\n next image")

    img_f.close()
    txt_f.close()
    lbl_f.close()


def main():
    img_file = Path(r'''C:\Users\steph\Downloads\mnist\train-images.idx3-ubyte.bin''')
    label_file = Path(r'''C:\Users\steph\Downloads\mnist\train-labels.idx1-ubyte.bin''')
    txt_file = Path(r'''C:\Users\steph\Downloads\mnist\mnist_train_1000_cntk.txt''')
    generate(img_file, label_file, txt_file, 1000) # 1-60,000

    img_file = Path(r'''C:\Users\steph\Downloads\mnist\t10k-images.idx3-ubyte.bin''')
    label_file = Path(r'''C:\Users\steph\Downloads\mnist\t10k-labels.idx1-ubyte.bin''')
    txt_file = Path(r'''C:\Users\steph\Downloads\mnist\mnist_test_100_cntk.txt''')
    generate(img_file, label_file, txt_file, 100) # 1-10,000

if __name__ == "__main__":
    main()
