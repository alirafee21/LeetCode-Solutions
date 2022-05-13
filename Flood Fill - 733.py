class Solution(object):

        
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        d_x = len(image)
        d_y = len(image[0])
       
        temp_col = image[sr][sc]
          def fill(sr,sc,color):

            if (sr >=d_x or sc >=d_y or sr<0 or sc<0 or image[sr][sc]!=temp_col or img[sr][sc] == newColor):
                return

            image[sr][sc] = newColor

            fill(image,sr+1,sc,newColor)

            fill(image,sr-1,sc,newColor)

            fill(image,sr,sc+1,newColor)

            fill(image,sr,sc-1,newColor)
        fill(sr,sc,)
           