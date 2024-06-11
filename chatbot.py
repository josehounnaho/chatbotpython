import streamlit as st

def chatbot_assistant(question):
    # Fonction pour répondre aux questions spécifiques en fonction du cours

    if "print en python" in question.lower():
        return """
        Pour écrire un print en Python, utilisez la fonction `print()` suivie de ce que vous voulez afficher entre parenthèses et guillemets. Par exemple : `print("Bonjour, monde!")`.
        """

    elif "indentation" in question.lower():
        return """
        En Python, l'indentation est cruciale pour définir la portée du code. Assurez-vous d'indenter chaque bloc de code, tel que les instructions conditionnelles (`if`, `else`, `elif`) et les boucles (`for`, `while`), avec 4 espaces ou une tabulation.
        """

    elif "appeler une variable" in question.lower() or "déclarer une variable" in question.lower():
        return """
        Pour déclarer une variable en Python, utilisez la syntaxe suivante : `nom_de_variable = valeur`. Par exemple : `age = 30` ou `nom = 'Alice'`.
        """

    elif "structures conditionnelles" in question.lower():
        return """
        En Python, utilisez les structures `if`, `elif` et `else` pour tester différentes conditions dans l'ordre. Voici un exemple :
        ```python
        if condition:
            # Code à exécuter si la condition est vraie
        elif autre_condition:
            # Code à exécuter si une autre condition est vraie
        else:
            # Code à exécuter si aucune des conditions précédentes n'est vraie
        ```
        """

    else:
        return "Je ne peux pas répondre à cette question pour le moment. Essayez une autre question."

def main():
    st.title("Chatbot Assistant pour le Cours Python")

    # Questions prédéfinies sous forme de boutons
    if st.button("Comment écrire un print en Python ?"):
        reponse = chatbot_assistant("print en python")
        st.markdown(f"**Réponse :** {reponse}")

    if st.button("Comment savoir si j'ai bien fait l'indentation en Python ?"):
        reponse = chatbot_assistant("indentation")
        st.markdown(f"**Réponse :** {reponse}")

    if st.button("Comment déclarer une variable en Python ?"):
        reponse = chatbot_assistant("déclarer une variable")
        st.markdown(f"**Réponse :** {reponse}")

    if st.button("Quelles sont les structures conditionnelles en Python ?"):
        reponse = chatbot_assistant("structures conditionnelles")
        st.markdown(f"**Réponse :** {reponse}")


    # Zone de texte pour la saisie de l'utilisateur
    question_utilisateur = st.text_input("Posez votre question ici :")

    # Bouton pour soumettre la question
    if st.button("Envoyer"):
        if question_utilisateur:
            # Appel de la fonction du chatbot pour obtenir la réponse
            reponse = chatbot_assistant(question_utilisateur)
            st.markdown(f"**Question :** {question_utilisateur}")
            st.markdown(f"**Réponse :** {reponse}")
        else:
            st.warning("Veuillez entrer une question avant de soumettre.")

if __name__ == "__main__":
    main()
