Here is the proposed patch for the failing client code:
```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return org.hamcrest.Matchers.containsString(java.lang.String.format("%s: Pushed", this.image.layer()));
}
```
Explanation:
The error message indicates that the `StringContains` constructor now requires only one argument, whereas previously it accepted two arguments. The new library version includes an overloaded `containsString` method in the `Matchers` class that can be used instead. This patch replaces the use of `StringContains` with the new `containsString` method.