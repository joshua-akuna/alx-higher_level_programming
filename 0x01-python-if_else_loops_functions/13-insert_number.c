#include "lists.h"

/**
 * insert_node - inserts a node into a linked list of type listint_t.
 * @head: a pointer to the linked list.
 * @number: an integer to stored it the new node.
 * Return: a pointer to the new node if successful else NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *prev = *head;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	else if (number < (*head)->n)
	{
		new_node->next = prev;
		*head = new_node;
	}

	while (prev->next && prev->next->n < number)
		prev = prev->next;

	if (prev->next == NULL)
		prev->next = new_node;
	else
	{
		new_node->next = prev->next;
		prev->next = new_node;
	}
	return (new_node);
}
