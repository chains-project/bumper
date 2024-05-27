Here is the proposed patch for the failing client code:
```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return org.hamcrest.CoreMatchers.containsString(java.lang.String.format("%s: Pushed", this.image.layer()));
}
```
Explanation:
The error message indicates that the `StringContains` constructor is expecting a single argument of type `String`, but is receiving two arguments: a `boolean` and a `String`.

Looking at the library changes, we can see that the `StringContains` constructor has been removed and replaced with a new method `containsString` in the `CoreMatchers` class.

Therefore, we can replace the `StringContains` constructor with the new `containsString` method.

Note that `CoreMatchers` is imported using the static import statement `import static org.hamcrest.CoreMatchers.*` for brevity.