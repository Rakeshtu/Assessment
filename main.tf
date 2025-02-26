provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "osv_rg" {
  name     = "osv-resource-group"
  location = "East US"
}

resource "azurerm_storage_account" "osv_storage" {
  name                     = "osvdatastorage"
  resource_group_name      = azurerm_resource_group.osv_rg.name
  location                 = azurerm_resource_group.osv_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "osv_container" {
  name                  = "osv-data"
  storage_account_name  = azurerm_storage_account.osv_storage.name
  container_access_type = "private"
}
