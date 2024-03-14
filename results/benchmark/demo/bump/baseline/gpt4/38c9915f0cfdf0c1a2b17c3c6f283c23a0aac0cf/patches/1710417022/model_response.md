It seems like the import statement is failing because the `LengthOf` class cannot be found in the `org.cactoos.iterable` package. This could be due to a number of reasons like the package does not exist, the class does not exist or the class has been moved to a different package in a newer version of the library.

Without knowing the exact details of the new version, it's hard to provide an exact solution. However, you can try to find the `LengthOf` class in the new version of the library and import it accordingly.

If the class has been moved to a different package, the import statement would look something like this:

```java
  import org.cactoos.SomeOtherPackage.LengthOf;
```

If the class has been renamed, the import statement would look something like this:

```java
  import org.cactoos.iterable.Length;
```

If the class has been removed entirely, you would need to find a replacement for it in the new version of the library. This could be another class or a combination of classes and methods. Without knowing the exact details of the new version, it's hard to provide an exact solution. However, the import statement would look something like this:

```java
  import org.cactoos.iterable.SomeReplacementClass;
```

Note: Replace `SomeOtherPackage`, `Length` and `SomeReplacementClass` with the actual package, class or method name in the new version of the library.