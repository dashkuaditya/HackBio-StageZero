


# Write a simple Python script for printing the names, slack username, country, 1 hobby, affiliations of people on your team and the DNA sequence of the genes they love most.

team_valine = [
   
{
        "name": "Tanshia Kumar",
        "slack_username": "@TANISHA KUMAR",
        "country": "Ireland",
        "hobby": "Reading books",
        "affiliation": "Student (university of galway, Galway), GUC",
        "favorite_gene": {
            "gene_name": "CSN2",
            "dna_sequence": "ATCATCCATCCAGCACTACCTTCACTTCTCTTCAATCTTGGAAAAACGGACTTAGTAGCCATGAAGGTCCTCATCCTCGCCTGCCTGGTGGC"
        }   
},


 {
        "name": "Sweeta Selvan",
        "slack_username": "@SWEETA SELVAN",
        "country": "India",
        "hobby": "Watching films",
        "affiliation": "Student (Anna University, Chennai), UAA",
        "favorite_gene": {
            "gene_name": "TP53",
            "dna_sequence": "ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACA"
        }   
},
{
        "name": "Aditya Dash",
        "slack_username": "@aditya dash",
        "country": "India",
        "hobby": "Playing cricket",
        "affiliation": "Student (Ravenshaw, Cuttack), GUU",
        "favorite_gene": {
            "gene_name": "BRCA1",
            "dna_sequence": "ATGGAAGTTGTCATTTTATAAAAAGGTTGCAAAATAATGTGGAAGAAAAAAAGCAGTGAACCTGTTGGTGATTTTGAAATGAGGAGGA"
        }  
},
    {
        "name": "Gloria Omogwigho Akpederi",
        "slack_username": "@Gloria Akpederi ",
        "country": "Nigeria",
        "hobby": "Baking",
        "affiliation": "Student (University of Lagos, Lagos), GUC" ,
        "favorite_gene": {
            "gene_name": "ACE2",
            "dna_sequence": "ATGGAGAGCCCTGTTCACATCTCCTCCTGCTCTCCTGCTCCTGCTCCTGCTCCTGGAGGAGGAGATCTTCCTCCTGCTGCTCTGCCT"
        }  
},
{
        "name": "Adarsh",
        "slack_username": " @Adarsh",
        "country": "India",
        "hobby": "singing",
        "affiliation": "Student (Sastra University,Thanjavur ), GUA",
        "favorite_gene": {
            "gene_name": "cd33",
            "dna_sequence": "ATGGCAAACACTGCTGAAGC"
        } 
}
]
# Print the information
for member in team_valine:
    print(f"Name: {member['name']}")
    print(f"Slack Username: {member['slack_username']}")
    print(f"Country: {member['country']}")
    print(f"Hobby: {member['hobby']}")
    print(f"Affiliation: {member['affiliation']}")
    print(f"Favorite Gene: {member['favorite_gene']['gene_name']}")
    print(f"DNA Sequence: {member['favorite_gene']['dna_sequence']}")
    print("-" * 20)