sup-rel
=======

A simple way of storing biological information where the relations
between individual objects are what matters the most.

Desired final functionality:
 - take a note in txt format.
 - Pull out Tag-terms (use # for tags)
 - Pull out persons (Use chained @to designate the persons)
 - Pull out the DOI ( use < > flag for this)
 - Store and index the full-text of the note + all the tags+al

Requirements:
 - a neo4j database instance
 
 Dependencies:
  - Neo4j 1.9.5 community server
  - Pyhton 2.7
  	- JPype1
  	- neo4j-embedded
  	- bulbs
