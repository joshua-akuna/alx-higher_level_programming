#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is
 *	a palindrome.
 * @head: a pointer the singly linked list.
 * Return: 1 if the singly linked list is a palindrome else 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *forward_node = *head;
	int node_count = 0;
	int forward_node_index, backward_node_index;
	int fval, bval;

	if (head == NULL || *head == NULL)
		return (0);

	while (forward_node->next != NULL)
	{
		node_count++;
		forward_node = forward_node->next;
	}

	forward_node_index = 0;
	backward_node_index = node_count;

	while (forward_node_index < backward_node_index)
	{
		fval = get_value_at_node_index(*head, forward_node_index);
		bval = get_value_at_node_index(*head, backward_node_index);
		/* printf("bval: %d ==> fval: %d ?\n", bval, fval); */
		if (fval != bval)
			return (0);
		forward_node_index++;
		backward_node_index--;
	}

	return (1);
}

/**
 * get_value_at_node_index - retrieves the value of the
 *	n property of a linked list node at a specified index.
 * @head: the head of the linked list.
 * @index: the specified index of the node whose n property
 *	we want to get.
 * Return: the value of the n property of the node at a
 *	specified index.
 */
int get_value_at_node_index(listint_t *head, int index)
{
	int i = 0;
	listint_t *ptr = head;

	while (ptr->next != NULL)
	{
		if (i == index)
			break;
		i++;
		ptr = ptr->next;
	}

	return (ptr->n);
}
