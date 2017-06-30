# Content
The content of the cube is represented by a 6x3x3 array, such that the first dimension of the array represents the face of the cube

The Front face is represented by the [0] array, the Up face is represented by the [1] array, the Right face is represented by the [2] array, the Back face is represented by the [3] array, the Down face is represented by the [4] array, and the Left face is represented by the [5] array.

This immediately gives us a useful relationship, where any face's opposite face is 3 away. We can make an easy getOppositeFace() function by adding 3 and reducing to mod6.

The coordinates of the stickers on the face are modeled after this image ![Rubiks cube](rubikscube/Rubik’s_cube_colors.svg.png)

# getEdge/getCorner
Each edge piece contains two stickers, where two faces meet. It would be useful to create a function that takes one edge sticker and returns the sticker on the other side of the edge.

Some of the stickers have clear patterns on where their other edge sticker lies. For instance, all of the Front stickers will have an edge sticker that has the coordinates of [x][2][1], and all of the Back stickers have an edge sticker with the coordinates of [x][0][1]

Therefore, if we are looking for a sticker whose coordinates are either [0][y][z] or [3][y][z], we know the result will be in the form of [a][2 or 0][1]. We can use these generalizations to make a smaller function of getEdge(x,y,z)


Each corner piece contains three stickers, where three faces meet. If we create a function that takes one corner sticker and returns the next sticker in a clockwise manner, we can feed that result back into the same function and get the third sticker.

Similarly some of these stickers have clear patterns on where their other corner sticker is.



Using the getEdge() function we can create a getEdgePiece(a,b) that checks each edge sticker to see if its contents are color a, and check the getEdge result to see if its contents are color b. Then it would return the results as a list, such that result[0-2] correspond to color a and result[3-5] correspond to color b.

Similarly we can use the getCorner() to create a getCornerPiece(a,b,c) to check each corner sticker and its adjacent stickers to find the corner piece that matches the colors we're looking for.

Since each edge piece and each corner piece are unique (each face only meets at an edge once and at a corner once), we know that getEdgePiece(a,b) and getCornerPiece(a,b,c) will return unique results.

# Rotating the Cube
To rotate a face, first the primary face is rotated 90 degrees. Then each of the adjoining faces will have one column or row shifted to another face. Because the cube is represented as 2d surfaces wrapped around a 3d object, the mapping will not always be smooth.

For instance, when we rotate the Front face, the 1st, 2nd and 3rd sticker of each adjoining face will be moved to the 1st, 2nd and 3rd sticker of the next face. However when we rotate the Up face, the 1st, 2nd, and 3rd sticker of the Front face will be moved to the 3rd, 6th, and 9th on the Left face.

To make it easier to swap the contents of the Left face, we can rotate it 270 degrees so that the 3rd, 6th and 9th sticker make up the first row. Then after all the faces are moved, the Left face is rotated 90 degrees back to the way it was.

# Solving the Cube
The solve function is the bulk of the program. It is separated into 7 main steps, each step solving looking for 4 different pieces, placing them in their proper position (permutation) and twisted the right way (orientation).

The permutation of a piece is its position in the cube. To permute a piece means to move it from one position to another. It is not possible to permute a piece without disturbing the permutation of atleast one other piece.

The orientation of a piece is its position of its stickers. An orientation is either 2bit or 3bit (edge/corner respectively). For instance an edge piece can be in the right spot on the cube but twisted so that both stickers are on the wrong face, similarly a corner piece can be in the right place but twisted clockwise or counterclockwise. It is not possible to orient a piece without affecting at least one other piece's orientation.

The first three steps solve for permutation and orientation simulatenously. This is easier in the first steps because there are a lot of unsolved pieces that can be moved or flipped without affecting the pieces already solved.

However, after these three steps, the bottom two layers are solved and only the top layer remains unsolved. Therefore, there is little space to move the pieces without affecting the solved pieces, so most algorithms are longer and less intuitive.

Once only the top layer remains, the orientation and permutation of the remaining pieces are forced into a limited number of possibilities. For instance, once the first two layers are solved, there can only be an even amount of edge pieces flipped up or down in the top layer. It is impossible for a valid cube to have 1 or 3 edge pieces flipped up or down in the top layer at this step.

Because the possibilities of orientation and permutation are limited, there are fewer cases to check. Using algorithms that only affect the orientation/permutation of the edge/corner pieces without affecting any of the other steps, we can solve for each of these in the last 4 steps.
