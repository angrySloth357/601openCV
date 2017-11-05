all:
	g++ -g -O2 `pkg-config --libs opencv` -o colorimg ColorImage.cpp 
	g++ -g -O2 `pkg-config --libs opencv` -o noise Noise.cpp 
	g++ -g -O2 `pkg-config --libs opencv` -o threshold Threshold.cpp 

.phony: clean

clean:
	rm -rf *.dSYM colorimg noise threshold
