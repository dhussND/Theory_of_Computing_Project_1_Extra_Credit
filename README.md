# Theory_of_Computing_Project_1_Extra_Credit

What was the extra work:
Providing test cases and a generator for the Hamiltonian path problem from project 1.

Why did you choose it (i.e. in what area did you feel deficient and how did this work help improve your understanding) You can point to specific homeworks or problem types on exams:
I chose to do it to provide other classmates working on the Hamiltonian path problem an easy way to validate the accuracy of their backtracking algorithm. This enriched my experience with Project 1 and I feel that I developed a deeper understanding in a number of areas. 

One of the primary goals of project 1 was for us to develop an appreciation for the exponential time increase as graph size increases. Because I was the one building these test cases, I got intimately familar with this property. I generated 130 graphs, 10 each between size 1 and 13. Initially, I had to plot the generated graphs and manually confirm whether or not a Hamiltonian path existed. Because I had to manually validate the graphs, I began to realize certain properties that allowed me to prune my backtracking algorithm. For example, in generating graphs of size n, I noticed that if the graph has fewer than n-1 edges, I could instantly decide no Hamiltonian path existed as that meant the graph was not connected.

This extra credit work also helped me further develop skills in other areas not directly related to Theory of Computing. Some of those skills included scripting as I needed to write a script to convert the .txt output to .cnf. I also had the opportunity to gain experience with the matplotlib library as I needed to generate graphs for each of my testcases so I could validate them. Additionally, the recommended networkx library for working with graphs was not available on the student machines, which required me to install and use WSL, giving me experience in an alternative development environment which was really useful. 

What files are what:
hamiltonian_path_test_cases2.txt - shows my test case in my default output format
hamiltonian_path_test_cases2.cnf - same as above, but in .cnf format
convert_to_cnf.py - function for converting .txt format to .cnf format
graph.png - one of the graphs shown as an image, which was used in validating my test case I provided for the class
hamiltonianPath.py (relevant functions: graph generator, graph plotter)
