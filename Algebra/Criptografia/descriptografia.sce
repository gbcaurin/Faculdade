// ALFABETO && TABELA DE INVERSOS

T = ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'];
TABELA = [1 3 5 7 9 11 15 17 19 21 23 25;1 9 21 15 3 19 7 23 11 5 17 25]

// MATRIZ CHAVE

A=[2 1;3 2]

deter=A(1,1)*A(2,2)-A(1,2)*A(2,1)
deter = pmodulo(deter,26)

// LOCALIZAR O DETERMINANTE NA TABELA DE INVERSOS

ind = find(deter==TABELA(1,:))
inverso = TABELA(2,ind)

// MATRIZ INVERSA

AI = inverso*[A(2,2) -A(1,2);-A(2,1) A(1,1)]

CIFRADO = ["G" "X" "C" "L"]
[m n]=size(CIFRADO)

for i=1:n
    I(:,i)=find(CIFRADO(:,i)==T)
end

// MATRIZ DO TEXTO CIFRADO

C=zeros(2,n/2)

// SEPARA DUPLAS DE SÍLABAS

for i=1:(n/2)
    k=2*i-1
    C(:,i)=[I(:,k); I(:,k+1)]
end

// DESCRIPTOGRAFIA

P=AI*C
P=pmodulo(P,26)

[r s]=size(P)

for i=1:r
    for j=1:s
     if P(i,j)==0 then P(i,j)=26
     else P(i,j)==P(i,j)    
    end   
    end 
end

// EXIBIR O TEXTO
P=P'

for i=1:(n/2)
    k=2*i-1
    TP(1,[k k+1])=P(i,:)
end

disp(T(1,TP))
