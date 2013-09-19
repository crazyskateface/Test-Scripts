using System;
using System.Data;
using System.Net;
using System.Xml.XPath;

namespace httpizzle
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			// ask for input of url from user
			Console.WriteLine ("Enter Feed URL: "); 
			// read in the url 
			string url = Console.ReadLine ();       
			// tell them something to make it interesting? ...
			Console.WriteLine ("Fetching RSS...");  
			
			//create a web request that gets the xml of a url specified
			HttpWebRequest rssFeed = (HttpWebRequest)WebRequest.Create(url); 				//"http://rss.cnn.com/rss/si_topstories.rss"  
						
			//use a new dataset called entries
			using (DataSet entries = new DataSet()){ 
				
				//read the xml feed from the given url and put it into entries
				entries.ReadXml (rssFeed.GetResponse ().GetResponseStream()); 
				
				//get the number of tables
				int c = entries.Tables.Count; 
				
				//create an array to store RssItems  ..or each article
				RssItem [] r = new RssItem[c+1]; 
				//counting for entering of rssitems
				int i = 0; 
				//get the title of the rssfeed  
				DataRow dr = entries.Tables["channel"].Rows[0]; 
				//store the title of the rssfeed
				string title = (string)dr["title"]; 
				//print the title of the rssfeed
				Console.WriteLine ("Feed: " + title);
				//print the number of entries/articles
				Console.WriteLine ("There are "+ c + " entries.\n");
				
				//This will loop through the entries and create an rssItem for each row corresponding to 'item' tags with their own tags: 'title' 'link' and 'description'
				foreach (DataRow dataRow in entries.Tables["item"].Rows){
					
					//create a new RssItem with each field needed as params
					RssItem rssitem = new RssItem((string)dataRow["title"], (string)dataRow["link"], (string)dataRow["description"]); 
					
					//add the rssitem to an array of RssItems
					r[i++] = rssitem; 
					
					//Console.WriteLine ("item = " + dataRow["title"]);
					//Console.WriteLine ("link = " + dataRow["link"]);
					
					
				}
				
				//character to compare for reading
				char read = 'r'; 
				//char skip = 's';
				//character to compare for quiting the program
				char quit = 'q'; 
				//character to compare the other characters to for user input
				char ans = 'r'; 
				//int used for iterating through a 'c' number of RssItems where c is the total number of them
				int count = 0;  
				
				//This is the main loop for input from the user to display entries 
				while(count <= c){
					//print out the title
					Console.WriteLine (r[count].Title); 
					//print out options
					Console.WriteLine ("Read (r), Skip (s), Quit (q): "); 
					//read in an option from user
					ans = Console.ReadLine ()[0]; 
					
					//print the description and link of the article if user input is 'r'
					if(ans.CompareTo (read)==0){
						Console.WriteLine (r[count].Description + "\n" + r[count].Link +"\n\n"); 
						}
					
					//if user has entered 'q' as input... quit out of the while loop
					else if(ans.CompareTo (quit)==0){
						Console.WriteLine ("Goodbye.\n"); 
						break;	
					}
					count++; //increment to the next article
				}
							
			}
						
		}
	}
	
	
	
	
	
	class RssItem{
		private string title;
		private string link;
		private string description;
		
		public RssItem(){
			this.title = "";
			this.link = "";
			this.description = "";
		}
		public RssItem (string title, string link, string description)
		{
			this.title = title;
			this.link = link;
			this.description = description;
		}
		public string Title {
			get {
				return this.title;
			}
			set {
				title = value;
			}
		}

		public string Link {
			get {
				return this.link;
			}
			set {
				link = value;
			}
		}
		
		public string Description {
			get {
				return this.description;
			}
			set {
				description = value;
			
			}
		}
	}
	
	class RssItems{
		private List<RssItem> rItems;
		
		public RssItems(){
			rItems = new List<RssItem>();
		}
		
		public RssItem Add(RssItem rItem){
			rItems.add(rItem);
		}
	}
}
