# input

def tranzactie(self, source, dest, value):
    self.source = source
    self.dest = dest
    self.value = value

tranzactii = []

with open('tranzactii.txt', 'r') as f:
    n = int(f.readline())
    for line in f.readlines():
        tranzactii.append(line.split())

# ma ajuta sa am sumele primite in int
for tranzactie in tranzactii:
    tranzactie[-1] = int(tranzactie[-1])


# toate chainurile gasite sunt stocate aici
found_chains = []

# pt a nu repeta chainurile intre ele. daca am gasit un nume intr-un chain deja existent, nu mai adaugam acel chain
banned_names = []


for tranzactie in tranzactii:
    # luam fiecare tranzactie si stocam sursa si suma de bani trimisa
    current_source = tranzactie[0]
    current_sum = tranzactie[-1]

    # link este destinatarul. el se schimba de fiecare data cand comparam tranzactia pe care am considerat-o initial cu toate celelalte
    link = tranzactie[1]

    # daca numele nu e in blacklist (nu avem niciun chain cu numele sursa in el), creaza un alt chain
    # observatie: un nume poate fi intr-un chain doar o singura data! cred..
    if current_source not in banned_names:

        current_chain = [current_source] # pt a fi mai usoara stocarea de chainuri, facem o lista dummy

        # pastram link-ul din moment ce se va schimba
        current_chain.append(link)

        while True:
            exit_flag = 0 # conditie de exit din loopul infinit
            for tranz in tranzactii:
                # daca gasim numele din link pe prima pozitie dintr-o tranzactie, dute pe acea tranzactie
                if tranz[0] == link:
                    link = tranz[1] # schimbam linkul
                    current_chain.append(link)
                    if tranz[2] < current_sum:
                        current_sum = tranz[2] # daca gasim o suma mai mica de bani, pastreaz-o
                    break
                else:
                    exit_flag = exit_flag + 1 # daca exit_flag va fi egal cu nr total de tranzactii, inseamca ca nu mai exista tranzactii pe care sa mergem / branchuim
            if exit_flag == n:
                break
            
        current_chain.append(current_sum)
        found_chains.append(current_chain)

        # punem fiecare nume din chain, mai putin suma (index -1), in blacklist
        banned_names = [*banned_names, *current_chain[:-1]]
        # print(banned_names)


# tot ce e de aici in jos e legat cu gasirea maximului din toate chainurile

max_len_chain = -1
max_chain_sum = -1
for chain in found_chains:
    if len(chain) > max_len_chain:
        max_len_chain = len(chain)

final_chains = []
for chain in found_chains:
    if len(chain) == max_len_chain:
        if chain[-1] > max_chain_sum:
            max_chain_sum = chain[-1]
        final_chains.append(chain)

result = 0
for chain in final_chains:
    if chain[-1] == max_chain_sum:
        result = chain

print(' '.join(result[:-1]))    # print chain
print(int(result[-1]))          # print sum