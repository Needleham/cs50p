from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, slogan):
        super().__init__()
        self.slogan = slogan

    def maker(self):
        self.add_page()
        self.image("shirtificate.png", x=0, y=0, w=0)
        self.set_font("helvetica", style="B", size=28)
        self.set_text_color(168)
        self.cell(w=0, h=150, text=f"{self.slogan}", border=0, align="C")

def slogan_gen():
    name = input("Name: ").strip()
    slogan = f"{name} took CS50"
    return slogan 


def main():
    slogan = slogan_gen()
    pdf = PDF(slogan)
    pdf.maker()
    pdf.output("final-certificate.pdf")

if __name__ == "__main__":
    main()


