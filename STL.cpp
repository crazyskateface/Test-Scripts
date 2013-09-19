#include <iostream>
//#include <stack>
//#include <vector>
//#include <algorithm>
//#include <string>
//#include <set>
//#include <map>
//#include <iterator>
//#include <sstream>
#include <cmath>

using namespace std;

 //typedef vector<int> vi; 
 //typedef vector<vi> vvi; 
 //typedef pair<int,int> ii; 
 //#define sz(a) int((a).size()) 
 //#define pb push_back 
 //#define all(c) (c).begin(),(c).end() 
 ////#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
 //#define present(c,x) ((c).find(x) != (c).end()) 
 //#define cpresent(c,x) (find(all(c),x) != (c).end())




 void MergeSort(int* data, int p, int r){
	 if( p < r ){
		 int mid = (p + r) /2;
		 int i1 = 0;
		 int i2 = p;
		 int i3 = mid +1;

		 //Temp array
		 int temp[r-p+1];

	 }



 }





 int main(){

	 //map<string, int> M;
	 //M["Top"] = 1;
	 //M["Coder"] = 2;
	 //M["SRM"] = 10;

	 //vector< pair<string, int> > V(all(M)); // remember all(c) stands for (c).begin(), (c).end();

	 //vector<int> v1;
	 //vector<int> v2;

	 //// copy v2 to the end of v1
	 //v1.resize(v1.size() + v2.size());
	 ////ensure v1 has enough space
	 //copy(all(v2), v1.end() - v2.size());
	 //// copy v2 elements right after v1 ones

	 //set<int> s;
	 ////ad some elements to set


	 //int data[10] = { 3,2, 1, 6, 5, 7, 9, 4, 8, 10};
	 //int N = sizeof data/sizeof(int); //length of array


	 ////bubble sort
	 //for(int i=0; i< N; i++){
		// for(int j=0; j<N -1; j++){
		//	 if(data[j] > data[j+1]){
		//		 int tmp = data[j];
		//		 data[j] = data[j+1];
		//		 data[j+1] = tmp;
		//	 }
		// }
	 //}

	 ////print 
	 //for(int i=0;i<N;i++){
		// cout << data[i];
	 //}cout << endl;

	 //int data[10] = { 3,2, 1, 6, 5, 7, 9, 4, 8, 10};
	 //int N = sizeof data/sizeof(int); //length of array

	 ////insertion sort - for data that is mostly already sorted
	 //for(int i=0; i <= N; i++){
		// int j=i;
		// while( j> 0 && data[i] < data[j-1])
		//	 j--;
		// int tmp = data[i];
		// for(int k =i; k > j; k--){
		//	 data[k] = data[k-1];
		// }
		// data[j] = tmp;
	 //}

	 int data[10] = { 3,2, 1, 6, 5, 7, 9, 4, 8, 10};
	 int N = sizeof data/sizeof(int); //length of array

	 //MERGE SORT
	 MergeSort(data);

	 return 0;

 }
