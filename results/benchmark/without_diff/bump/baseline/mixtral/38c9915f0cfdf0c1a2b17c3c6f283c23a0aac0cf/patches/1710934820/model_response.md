It seems the issue is caused by a missing dependency import. To resolve the error, you need to include the Cactoos library in your project's dependencies. If you are using Maven, add the following dependency to your `pom.xml`:

```xml
<dependency>
  <groupId>org.cactoos</groupId>
  <artifactId>cactoos</artifactId>
  <version>2.3</version>
</dependency>
```

If you have already included the Cactoos library in your project, make sure the version you are using is compatible with the version of the `JoinedText` class you are trying to use.

Assuming the dependency is correctly added, you can apply the following patch to fix the error:

```java
-import org.cactoos.text.JoinedText;
+import org.cactoos.text.Joined;

-  new JoinedText(", ", new TextOf(currencies));
+  new Joined(", ", currencies);
```

The `TextOf` class has been removed from Cactoos 2.3, and the `JoinedText` constructor now accepts an Iterable of Text directly. By using `Joined` instead, you ensure compatibility with both new and old versions of Cactoos.