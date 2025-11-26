from .main_preprocessing import main as preprocessing
from .main_ARM import main as arm


def main():
  preprocessing()
  arm()


if __name__ == "__main__":
  main()
