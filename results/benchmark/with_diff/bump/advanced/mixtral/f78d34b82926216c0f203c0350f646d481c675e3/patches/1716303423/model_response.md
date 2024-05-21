Here is a patched version of the client code that uses the new library version:
```java
import tokyo.peya.lib.WaveCreator;
```
This code imports the `WaveCreator` class from the new package `tokyo.peya.lib` instead of `develop.p2p.lib`. This should fix the "package does not exist" error you were seeing.