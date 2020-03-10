# openstax-intern-assessment
I have my read_greetings.py inside the code folder. 

Build the Dockerfile using command: docker build -t openstax-intern-assessment .
Run the image: docker run --rm -v $PWD:$PWD openstax-intern-assessment python /read_greetings.py $PWD/greetings.xml

I changed the command from '/code/read_greetings.py" to just "/read_greetings.py". It couldn't find the read_greetings.py 
in that way. 
