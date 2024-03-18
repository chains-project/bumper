The error message indicates that the import statement is incorrect. Without the full context of the changes in the new library version, it's impossible to provide the precise solution. However, it seems like the class `UncheckedText` might have been moved to a different package or renamed. 

You should look into the new library's documentation or source code to find out where `UncheckedText` is now located or what it has been renamed to, and update the import statement accordingly. 

If, for example, it has been renamed to `TextUnchecked`, the updated import statement would look like:

```java
import org.cactoos.text.TextUnchecked;
```

If it has been moved to a different package, the import statement should be updated to reflect this. For example, if it has been moved to `org.cactoos`:

```java
import org.cactoos.UncheckedText;
```

In either case, the rest of your code might also need to be updated to use the new class name or package.