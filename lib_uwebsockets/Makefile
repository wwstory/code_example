EXE := demo

CXXFLAGS += `pkg-config --cflags opencv4`
LIBS += `pkg-config --libs opencv4`

USOCKET_DIR = include/uSockets
CXXFLAGS += -std=c++17 -Iinclude -Iinclude/uSockets/src
LDFLAGS += $(USOCKET_DIR)/*.o -lz


all: usocket main

.PHONY: usocket
usocket:
	cd $(USOCKET_DIR) && WITH_SSL=0 make

.PHONY: clean_usocket
clean_usocket:
	rm -f include/uSockets/*.o

.PHONY: main
main:
	$(CXX) $(CXXFLAGS) $(EXE).cpp -o $(EXE) $(LIBS) $(LDFLAGS)

.PHONY: clean
clean: clean_usocket
	rm -f $(EXE)

.PHONY: test
test: clean
	make all
	./$(EXE)
