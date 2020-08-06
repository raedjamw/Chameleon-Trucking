# -*- coding: utf-8 -*-
"""NNeigh.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vLPeGocccoHao1N4zZwWJSpY_gNM7oVF

NAIVE VERSION of the K Nearest Neighbor Algorithm for K = 2,Modified from the Source:-https://automating-gis-processes.github.io/site/notebooks/L3/nearest-neighbor-faster.html
"""

# Imports
from sklearn.neighbors import BallTree

def get_nearest(src_points, candidates, k_neighbors=2):
  """
    converts lat-long coords to great-circle distance and
    returns the two closests
  """

  # Create tree from the candidate points
    tree = BallTree(candidates, leaf_size=20, metric='haversine')

    # Find closest points and distances
    distances, indices = tree.query(src_points, k=k_neighbors)

    # Transpose to get distances and indices into arrays
    distances = distances.transpose()
    indices = indices.transpose()

    #Get closest indices and distances (i.e. array at index 0)
    #note: for the second closest points, you would take index 1, etc.
    closest = indices[0:2]
    closest_dist = distances[0:2]


    return (closest, closest_dist)


def nearest_neighbor(left_gdf, right_gdf, return_dist=False):
    """
    For each point in left_gdf, find closest 2 points in right GeoDataFrame,
    convert to meters and return them.

    NOTICE: Assumes that the input Points are in WGS84 projection (lat/lon).
    
    """
    left_geom_col = left_gdf.geometry.name

    right_geom_col = right_gdf.geometry.name

    # indicies in right_gdf are ordered numbers
    right = right_gdf.copy().reset_index(drop=True)

    # Parse dfs for geometry columns and convert them to Radians in a np arrat
    left_radians = np.array(left_gdf[left_geom_col].apply(lambda geom: (geom.x * np.pi / 180, geom.y * np.pi / 180)).tolist())
    right_radians = np.array(right[right_geom_col].apply(lambda geom: (geom.x * np.pi / 180, geom.y * np.pi / 180)).tolist())
 
    # Find the nearest points
    # -----------------------
    # closest ==> index in right_gdf that corresponds to the closest point
    # dist ==> distance between the nearest neighbors (in meters)

    closest, dist = get_nearest(src_points = left_radians, candidates=right_radians)

    # Return points from right df that are closest to those in the left df
    closest_points = right.loc[closest[0]]
    t_closest_points = right.loc[closest[1]]

    # Ensure that the index corresponds the one in left_gdf
    closest_points = closest_points.reset_index(drop=True)

    t_closest_points = t_closest_points.reset_index(drop=True)
    # Add distance if requested

    for i in range(0,len(dist)):
      if return_dist:
        # Convert radians to meters 
        earth_radius = 6371000  
        closest_points['distance in meters_{}'.format(i+1)] = dist[i] * earth_radius

    return closest_points

def main():
  get_nearest()
  nearest_neighbor()

if __name__ == "__main__":
    main()