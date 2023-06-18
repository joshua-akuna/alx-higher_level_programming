#include "lists.h"

/**
 * check_cycle-checks if a single linked list has a cycle in it.
 * @list: a singly linked list.
 * Return: 1 if the singly linked list has a cycle in it else 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *front, *rear;

	front = rear = list;
	while (front != NULL && front->next != NULL)
	{
		front = front->next->next;
		rear = rear->next;

		if (front == rear)
			return (1);
	}
	return (0);
}
