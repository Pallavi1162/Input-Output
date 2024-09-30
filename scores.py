'''
I/O - Q3:
It was in the 1997-98 season that Ranchi saw the rise of the Captain Cool in the interschool trophy between DAV Jawahar Vidhya Mandir and Kendriya School. It was in that match Dhoni convinced Banerjee to be the opener and justified it with a double century.
Write a program to display the details of the match with Team name, Scores of the team and Overs played.
Input and Output Format:  
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and the rest corresponds to output]
Sample Input and Output:
Team 1:
Team Name:
DAV Jawahar Vidhya Mandir
Score:
150
Overs played:
20
Team 2:
Team name:
Kendriya School
Score:
110
Overs played:
18
Match Details:
Team 1:
Name: DAV Jawahar Vidhya Mandir
Score: 150
Overs played: 20
Team 2:
Name:  Kendriya School
Score: 110
Overs played: 18

'''

match_details={
  "team1":input("enter team name:\n"),
  "score":input("score:\n"),
  "overs":input("overs played:\n"),
  "team2":input("enter team name:\n"),
  "score":input("score:\n"),
  "overs":input("overs played:\n")
}
print("\nMatch Details:\n")
print("*------------------------------------*")
print()
print(f"Team1:{match_details['team1']}")
print(f"score:{match_details['score']}")
print(f"Overs Played:{match_details['overs']}")
print()
print(f"Team2:{match_details['team2']}")
print(f"score:{match_details['score']}")
print(f"overs Played:{match_details['overs']}")

