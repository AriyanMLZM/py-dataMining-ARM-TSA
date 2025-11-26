from main_preprocessing import main as preprocessing
from main_ARM import main as arm
from main_TSA import main as tsa


def main():
  preprocessing()
  arm()
  tsa()


if __name__ == "__main__":
  main()
