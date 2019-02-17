echo "########## Instalação de dependencias ############"
echo "Caso necessário, configure seu ambiente pyenv para 3.6.4"

pyenv shell 3.6.4

python3 -m pip install Pillow
pip install pytesseract
pip install opencv-python
brew install tesseract
pip install mahotas