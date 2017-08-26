#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <string.h>

using namespace std;



int main()
{
	ifstream output,realoutput;
	output.open("output.txt",ios::binary);
	realoutput.open("realoutput.txt",ios::binary);
	char string1[256], string2[256];
	string getcontent;
	int j = 0;
	int flag =0;
	while(!output.eof())
	{
		output.getline(string1,256);
		realoutput.getline(string2,256);
		j++;
		if(strcmp(string1,string2) != 0)
		{
			flag = 1;
			cout <<"Output "<<j<< " doesnt match" << "\n";
			cout << "Your Output:   " << string1 << "\n";
			cout << "Expected Output:  " << string2 << "\n";
		}
	}
	output.close();
	realoutput.close();
	if(flag == 0)
		cout <<"All test cases passed successfully\n";
	else{
		 output.open("output.txt");
		 cout << "Your Output: " <<endl;
		 if(output.is_open())
		{
			while(getline(output, getcontent))
			{
			
            cout << getcontent << endl;
			}
		}
		realoutput.open("realoutput.txt");
		cout << "Expected Output: " <<endl;
		 if(realoutput.is_open())
		{
			while(getline(realoutput, getcontent))
			{
            cout << getcontent << endl;
			}
		}
    }
	
	return 0;
}
