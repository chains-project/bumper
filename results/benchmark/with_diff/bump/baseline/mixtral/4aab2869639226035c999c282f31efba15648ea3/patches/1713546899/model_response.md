Sure, based on the information provided, it seems that the `Storages` class has been removed and replaced with `StoragesLoader` in the new version of the library. Here's a possible patch that you can apply to the code:
```java
import com.artipie.asto.factory.StoragesLoader;

// ...

StoragesLoader storagesLoader = new StoragesLoader();
```
Then, you can use the `storagesLoader` object to create `Storage` objects in your code. For example, if you previously created a `Storage` object like this:
```java
Storages storages = Storages.single("my-storage", config);
Storage storage = storages.newStorage("my-storage", config);
```
You can now create it like this:
```java
Storage storage = storagesLoader.newObject("my-storage", config);
```
Note that the `newStorage` method of `StoragesLoader` takes a `Config` object instead of a `StorageConfig` object. If you need to convert a `StorageConfig` object to a `Config` object, you can do it like this:
```java
Config config = ConfigConverter.convert(storageConfig);
```
Assuming that you have a `ConfigConverter` class that can convert a `StorageConfig` object to a `Config` object. You may need to modify this code based on the specifics of your use case.