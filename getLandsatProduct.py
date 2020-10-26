import ee

# Authenticating earth engine
ee.Authenticate()

# Initializing earth engine
ee.Initialize()

# Assigning values that are required in upcoming function
sensor_slice = slice(4)
processing_level_slice = slice(5, 9, 1)
image_number_slice = slice(10, 25, 1)
collection_number_slice = slice(35, 37, 1)
collection_category_slice = slice(38, 40, 1)

# Function to filter out the sentinel product id and select the satellite image.

def getLandsatProductById(productId):

    if productId[sensor_slice] == 'LE07':
        spatial_resolution = 30
        bands = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6_VCID_1', 'B6_VCID_2', 'B7', 'B8']

        ### Landsat 7 Collection 1 Tier 1 Raw Scenes
        if productId[processing_level_slice] == 'L1TP' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T1':   
            collection_id = 'LANDSAT/LE07/C01/T1/'
            folder = 'L07_Tier_1'

        ### Landsat 7 Collection 1 Tier 2 Raw Scenes
        elif productId[processing_level_slice] == 'L1TP' or 'L1GT' or 'L1GS' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T2':
            collection_id = 'LANDSAT/LE07/C01/T2/'
            folder = 'L07_Tier_2'

    ### Landsat 5 Thematics Mapper 
    elif productId[sensor_slice] == 'LT05':
        spatial_resolution = 30
        bands = ['B1', 'B2', 'B3', 'B4']

        ### Landsat 5 TM Collection 1 Tier 1 Raw Scenes
        if productId[processing_level_slice] == 'L1TP' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T1':
            collection_id = 'LANDSAT/LT05/C01/T1/'
            folder = 'L_05_TM_Tier_1'

        ### Landsat 5 TM Collection 1 Tier 2 Raw Scenes
        elif productId[processing_level_slice] == 'L1TP' or 'L1GT' or 'L1GS' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T2':
            collection_id = 'LANDSAT/LT05/C01/T2/'
            folder = 'L05_TM_Tier_2'

    ### Landsat 5 MSS
    elif productId[sensor_slice] == 'LM05':
        spatial_resolution = 60
        bands = ['B1', 'B2', 'B3', 'B4']

        ### Landsat 5 MSS Collection 1 Tier 1 Raw Scenes
        if productId[processing_level_slice] == 'L1TP' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T1':
            collection_id = 'LANDSAT/LM05/C01/T1/'
            folder = 'L05_MSS_Tier_1'

        ### Landsat 5 MSS Collection 1 Tier 2 Raw Scenes
        elif productId[processing_level_slice] == 'L1TP' or 'L1GT' or 'L1GS' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T2':
            collection_id = 'LANDSAT/LM05/C01/T2/'
            folder = 'L05_MSS_Tier_2'

    ### Landsat 4 Thematics Mapper 
    elif productId[sensor_slice] == 'LT04':
        spatial_resolution = 30
        bands = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']

        ### Landsat 4 TM Collection 1 Tier 1 Raw Scenes
        if productId[processing_level_slice] == 'L1TP' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T1':
            collection_id = 'LANDSAT/LT04/C01/T1/'
            folder = 'L04_TM_Tier_1'

        ### Landsat 4 TM Collection 1 Tier 2 Raw Scenes
        elif productId[processing_level_slice] == 'L1TP' or 'L1GT' or 'L1GS' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T2':
            collection_id = 'LANDSAT/LT04/C01/T2/'
            folder = 'L04_TM_Tier_2'

    ### Landsat 4 MSS
    elif productId[sensor_slice] == 'LM04':
        spatial_resolution = 60
        bands = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']

        ### Landsat 4 MSS Collection 1 Tier 1 Raw Scenes
        if productId[processing_level_slice] == 'L1TP' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T1':
            collection_id = 'LANDSAT/LM04/C01/T1/'
            folder = 'L04_MSS_Tier_1'

        ### Landsat 4 MSS Collection 1 Tier 2 Raw Scenes
        elif productId[processing_level_slice] == 'L1TP' or 'L1GT' or 'L1GS' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T2':
            collection_id = 'LANDSAT/LM04/C01/T2/'
            folder = 'L04_MSS_Tier_2'

    ### Landsat 3 MSS
    elif productId[sensor_slice] == 'LM03':
        spatial_resolution = 60
        bands = ['B4', 'B5', 'B6', 'B7']

        ### Landsat 3 MSS Collection 1 Tier 1 Raw Scenes
        if productId[processing_level_slice] == 'L1TP' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T1':
            collection_id = 'LANDSAT/LM03/C01/T1/'
            folder = 'L03_MSS_Tier_1'

        ### Landsat 3 MSS Collection 1 Tier 2 Raw Scenes
        elif productId[processing_level_slice] == 'L1TP' or 'L1GT' or 'L1GS' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T2':
            collection_id = 'LANDSAT/LM03/C01/T2/'
            folder = 'L03_MSS_Tier_2'

    ### Landsat 2 MSS
    elif productId[sensor_slice] == 'LM02':
        spatial_resolution = 60
        bands = ['B4', 'B5', 'B6', 'B7']

        ### Landsat 2 MSS Collection 1 Tier 1 Raw Scenes
        if productId[processing_level_slice] == 'L1TP' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T1':
            collection_id = 'LANDSAT/LM02/C01/T1/'
            folder = 'L02_MSS_Tier_1'

        ### Landsat 2 MSS Collection 1 Tier 2 Raw Scenes
        elif productId[processing_level_slice] == 'L1TP' or 'L1GT' or 'L1GS' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T2':
            collection_id = 'LANDSAT/LM02/C01/T2/'
            folder = 'L02_MSS_Tier_2'

    ### Landsat 1 MSS
    elif productId[sensor_slice] == 'LM01':
        spatial_resolution = 60
        bands = ['B4', 'B5', 'B6', 'B7']

        ### Landsat 1 MSS Collection 1 Tier 1 Raw Scenes
        if productId[processing_level_slice] == 'L1TP' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T1':
            collection_id = 'LANDSAT/LM01/C01/T1/'
            folder = 'L01_MSS_Tier_1'

        ### Landsat 1 MSS Collection 1 Tier 2 Raw Scenes
        elif productId[processing_level_slice] == 'L1TP' or 'L1GT' or 'L1GS' and productId[collection_number_slice] == '01' and productId[collection_category_slice] == 'T2':
            collection_id = 'LANDSAT/LM01/C01/T2/'
            folder = 'L01_MSS_Tier_2'

    else:
        print('Image not found for LANDSAT_PRODUCT ID ' + productId + '.')

    product = ee.Image(collection_id + productId[sensor_slice] + '_' + productId[image_number_slice])
    product = product.select(bands)
    
    # Exporting image to google drive with specific parametes
    Task = ee.batch.Export.image.toDrive(**{
    'image': product,
    'description': productId,
    'folder': folder,
    'scale': spatial_resolution
    })

    Task.start()

