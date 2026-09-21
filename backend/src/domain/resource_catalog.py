from dataclasses import asdict, dataclass

from models.schemas import DeploymentManifest, ResourceKey


@dataclass(frozen=True)
class CatalogEntry:
    label: str
    module: str
    dependencies: tuple[ResourceKey, ...] = ()


RESOURCE_CATALOG: dict[ResourceKey, CatalogEntry] = {
    "foundry": CatalogEntry(
        "Project in the platform Microsoft Foundry account", "modules/foundry.bicep"
    ),
    "chat-model": CatalogEntry(
        "Workload chat model deployment", "modules/foundry.bicep", ("foundry",)
    ),
    "embedding-model": CatalogEntry(
        "Workload embedding model deployment", "modules/foundry.bicep", ("foundry",)
    ),
    "managed-identity": CatalogEntry(
        "Platform-managed identity reference", "main.bicep"
    ),
    "storage": CatalogEntry(
        "Container in the platform Storage account", "modules/storage-container.bicep"
    ),
    "cosmos": CatalogEntry(
        "Container in the platform Cosmos DB database", "modules/cosmos-container.bicep"
    ),
    "ai-search": CatalogEntry(
        "Existing platform Azure AI Search index reference", "main.bicep"
    ),
    "observability": CatalogEntry(
        "Platform observability reference", "main.bicep"
    ),
    "private-network": CatalogEntry(
        "Platform private network boundary", "main.bicep"
    ),
}


def resolve_resources(requested: list[ResourceKey]) -> list[ResourceKey]:
    resolved: list[ResourceKey] = []

    def visit(key: ResourceKey) -> None:
        if key in resolved:
            return
        for dependency in RESOURCE_CATALOG[key].dependencies:
            visit(dependency)
        resolved.append(key)

    for key in requested:
        visit(key)
    return resolved


def describe_resources(keys: list[ResourceKey]) -> list[dict[str, object]]:
    return [{"key": key, **asdict(RESOURCE_CATALOG[key])} for key in keys]


def to_bicep_parameters(manifest: DeploymentManifest) -> dict[str, object]:
    platform = manifest.platform_resources
    return {
        "workloadName": manifest.workload_name,
        "storageResourceGroupName": platform.storage_resource_group,
        "storageAccountName": platform.storage_account_name,
    }
