Here is a fixed version of the `layersPushed` method that should resolve the error:
```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return new org.hamcrest.core.IsNot(new org.hamcrest.core.StringContains(java.lang.String.format("%s: Pushed", this.image.layer()))));
}
```
In the new version of the library, the `StringContains` constructor no longer accepts a boolean parameter. Instead, we can use the `IsNot` matcher to achieve the same effect.