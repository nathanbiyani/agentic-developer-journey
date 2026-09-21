targetScope = 'subscription'

param workloadName string
param deploymentStamp string
param storageResourceGroupName string
param storageAccountName string

var suffix = take(toLower(deploymentStamp), 6)
var blobContainerName = take(toLower('${workloadName}-${suffix}'), 63)

module storage './modules/storage-container.bicep' = {
  name: 'checkout-storage-${suffix}'
  scope: resourceGroup(storageResourceGroupName)
  params: {
    accountName: storageAccountName
    containerName: blobContainerName
  }
}

output deployment object = {
  storageAccountName: storageAccountName
  storageResourceId: resourceId(subscription().subscriptionId, storageResourceGroupName, 'Microsoft.Storage/storageAccounts', storageAccountName)
  storageBlobEndpoint: 'https://${storageAccountName}.blob.${environment().suffixes.storage}'
  storageContainerName: storage.outputs.containerName
  storageContainerResourceId: storage.outputs.containerResourceId
}
