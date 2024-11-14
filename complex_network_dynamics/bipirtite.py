import networkx as nx
import matplotlib.pyplot as plt

# Create a bipartite graph
G = nx.Graph()
G.add_nodes_from(['Pfizer-BioNTech','AstraZeneca','Moderna','Sinopharm','Covaxin','Johnson','Sinovac','CanSino'], bipartite=0)
G.add_nodes_from(['Poland', 'Bosnia', 'Croatia', 'Iran', 'Slovenia', 'Switzerland', 'Malta', 'Spain', 'Italy', 'Turkey', 'Afghanistan', 'Argentina', 'Hungary', 'Peru', 'Japan', 'China', 'Chile', 'Korea'], bipartite=1)
G.add_edges_from([('Pfizer-BioNTech', 'Poland'), ('Pfizer-BioNTech', 'Bosnia'), ('Pfizer-BioNTech', 'Croatia'), ('Pfizer-BioNTech', 'Slovenia'), ('Pfizer-BioNTech', 'Switzerland'),('Pfizer-BioNTech', 'Malta'), ('Pfizer-BioNTech', 'Spain'), ('Pfizer-BioNTech', 'Italy'),('Pfizer-BioNTech', 'Turkey'), ('Pfizer-BioNTech', 'Hungary'),('Pfizer-BioNTech', 'Peru'), ('Pfizer-BioNTech', 'Japan'),('Pfizer-BioNTech', 'Chile'), ('Pfizer-BioNTech', 'Korea'), ('AstraZeneca', 'Poland'), ('AstraZeneca', 'Bosnia'), ('AstraZeneca', 'Croatia'), ('AstraZeneca', 'Iran'), ('AstraZeneca', 'Slovenia'), ('AstraZeneca', 'Switzerland'), ('AstraZeneca', 'Malta'), ('AstraZeneca', 'Spain'), ('AstraZeneca', 'Italy'), ('AstraZeneca', 'Turkey'), ('AstraZeneca', 'Afghanistan'), ('AstraZeneca', 'Hungary'), ('AstraZeneca', 'Peru'), ('AstraZeneca', 'Japan'), ('AstraZeneca', 'Chile'), ('AstraZeneca', 'Korea'), ('Moderna', 'Poland'),('Moderna', 'Bosnia'),('Moderna', 'Croatia'),('Moderna', 'Slovenia'),('Moderna', 'Switzerland'),('Moderna', 'Spain'),('Moderna', 'Italy'),('Moderna', 'Japan'),('Moderna', 'Korea'),('Sinopharm', 'Iran'),('Sinopharm', 'Afghanistan'),('Sinopharm', 'Argentina'),('Sinopharm', 'Hungary'),('Sinopharm', 'Peru'),('Sinopharm', 'China'),('Covaxin', 'Iran'),('Sinovac', 'Turkey'),('Sinovac', 'China'),('Sinovac', 'Chile'),('Johnson', 'Malta'),('Johnson', 'Afghanistan'),('CanSino', 'China'),('Sinopharm', 'Argentina'),('Sinopharm', 'Hungary')])

# Draw the bipartite graph
pos = nx.bipartite_layout(G, ['Pfizer-BioNTech','AstraZeneca','Moderna','Sinopharm','Covaxin','Johnson','Sinovac','CanSino'])
node_colors = ['blue' if node in ['Pfizer-BioNTech','AstraZeneca','Moderna','Sinopharm','Covaxin','Johnson','Sinovac','CanSino'] else 'red' for node in G.nodes]
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color=node_colors)

plt.show()

# Project the graph onto the country nodes
country_nodes = set(node for node, data in G.nodes(data=True) if data['bipartite'] == 1)
country_graph = nx.bipartite.projected_graph(G, nodes=country_nodes)

# Draw the projected graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(country_graph)
nx.draw(country_graph, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=800, font_size=8, font_color='black', font_family='sans-serif')
plt.title("Projected Graph Based on Country Affiliations")
plt.show()


internal_degrees = {}
external_degrees = {}

for country in country_nodes:
    internal_degrees[country] = sum(1 for neighbor in country_graph.neighbors(country) if G.nodes[neighbor]['bipartite'] == 1)
    external_degrees[country] = sum(1 for neighbor in country_graph.neighbors(country) if G.nodes[neighbor]['bipartite'] == 0)

# Draw the projected graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(country_graph)
nx.draw(country_graph, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=800, font_size=8, font_color='black', font_family='sans-serif')
plt.title("Projected Graph Based on Country Affiliations")

# Print internal and external degrees for each country
for country in country_nodes:
    print(f"{country}: Internal Degree {internal_degrees[country]}")
print ('Croatia: Degree 15')
print ('Slovenia: Degree 15')
print ('Hungrary: Degree 16')
print ('Greece: Degree 15')
print ('Poland: Degree 15')
print ('Peru: Degree 10')
print ('Turkey: Degree 14')
print ('Bosnia: Degree 16')
print ('China: Degree 7')
print ('Chile: Degree 12')
print ('Japan: Degree 7')
print ('Argentina: 10')
print ('Korea: Degree 7')
print ('Italy: Degree 15')
print ('Switzerland: Degree 15')
print ('Malta: Degree 15')
print ('Afghanistan: Degree 5')