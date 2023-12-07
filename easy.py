{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2914be4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "4\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "def length_of_last_word(s):\n",
    "    s = s.rstrip()\n",
    "    length = 0\n",
    "    for char in reversed(s):\n",
    "        if char == ' ':\n",
    "            break\n",
    "        length += 1\n",
    "\n",
    "    return length\n",
    "\n",
    "print(length_of_last_word(\"Hello World\")) \n",
    "print(length_of_last_word(\"   fly me   to   the moon  \")) \n",
    "print(length_of_last_word(\"luffy is still joyboy\")) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ecdd284",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
