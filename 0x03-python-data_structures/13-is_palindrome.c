#include "lists.h"

/**
 * is_palindrome - checks if a sll is a palindrome
 * @head: head of sll
 *
 * Return: 1 for true, 0 for false
 */
int is_palindrome(listint_t **head)
{
	int len = 0;
	int jump, i, j, len_d_2;
	listint_t *temp1 = (*head);
	listint_t *temp2 = (*head);

	if (!(*head))
		return (1);

	if (len == 0)
	{
		while (temp1->next)
		{
			temp1 = temp1->next;
			len++;
		}
		len++;
		if (temp2->n != temp1->n)
			return (0);
	}

	if (len == 1)
		return (1);

	len_d_2 = len / 2;
	jump = len - 1 - 2;

	for (i = 1; i < len_d_2; i++, jump -= 2)
	{
		temp2 = temp2->next;
		temp1 = temp2;
		for (j = 0; j < jump; j++)
			temp1 = temp1->next;
		if (temp2->n != temp1->n)
			return (0);
	}
	return (1);

}
