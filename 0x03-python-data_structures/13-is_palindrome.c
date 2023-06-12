#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is
 *	a palindrome.
 * @head: a pointer the singly linked list.
 * Return: 1 if the singly linked list is a palindrome else 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *front, *rear, *next, *prev;

	if (head == NULL || *head == NULL)
		return (1);

	front = *head;
	rear = *head;
	prev = NULL;

	while (front != NULL && front->next != NULL)
	{
		front = front->next->next;
		next = rear->next;
		rear->next = prev;
		prev = rear;
		rear = next;
	}

	if (front != NULL)
		rear = rear->next;

	while (prev != NULL && rear != NULL)
	{
		if (prev->n != rear->n)
			return (0);
		prev = prev->next;
		rear = rear->next;
	}
	return (1);
}
