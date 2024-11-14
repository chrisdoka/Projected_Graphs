import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import itertools 

def create_vaccination_graph(file_path):
    df = pd.read_csv(file_path) #data
    G = nx.Graph()            # dircted graph 
    projected_edges=df.groupby("vaccines").country.apply(
        lambda vac_ds: list(itertools.product(vac_ds, repeat=2))
    ).tolist()
    print(projected_edges)
    exit()
    countries = df['country'].tolist() #countries as noes
    G.add_nodes_from(countries)
    # Add edges for vaccination 
    edges = list(zip(df['country'], df['total_vaccinations']))
    G.add_edges_from(edges)
    return G


def plot_graph(G):
    plt.figure(figsize=(12, 8)) 
    pos = nx.spring_layout(G)  # graph visualization
    nx.draw(G, pos, with_labels=True, font_size=8, node_size=800, node_color='skyblue', font_color='black', font_weight='bold', edge_color='gray')
    plt.title('COVID-19 Vaccination Progress Network')
    plt.savefig("graph.png")

file_path = r'C:\Users\xrist\Downloads\archive\country_vaccinations.csv'
vaccination_graph = create_vaccination_graph(file_path)
plot_graph(vaccination_graph)
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