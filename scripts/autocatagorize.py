layer = next(lyr for lyr in QgsProject.instance().mapLayers().values() if 'description' in lyr.fields().names())

if not layer.isEditable():
    layer.startEditing()

if layer.fields().indexOf('auto_category') == -1:
    layer.dataProvider().addAttributes([QgsField('auto_category', QVariant.String)])
    layer.updateFields()

idx = layer.fields().indexOf('auto_category')

for feature in layer.getFeatures():
    if feature['ele'] and feature['ele'] > 2000:
        layer.changeAttributeValue(feature.id(), idx, 'High Altitude')
    else:
        layer.changeAttributeValue(feature.id(), idx, 'Standard')

layer.commitChanges()
print("Done! Categorized all features.")