Here is a possible patch for the client code:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(),
        coverage.getClassInfo(data.getMutatedClass()).getSingleClassInfo());
}
```

In the original code, the `getClassInfo` method of the `CoverageDatabase` class is called with a set of class names as an argument. However, this method has been removed in the new library version.

Instead, the `getClassInfo` method of the `CoverageDatabase` class can now be called with a single class name as an argument, and it returns a `ClassInfo` object. To get the `ClassInfo` object for a single class, you can use the `getSingleClassInfo` method of the `ClassInfoBuilder` class.

Therefore, in the patched code, the `getClassInfo` method is called with a single class name (`data.getMutatedClass()`) as an argument, and the `getSingleClassInfo` method is called on the `ClassInfo` object returned by `getClassInfo`. This should fix the error caused by the removed `getClassInfo` method.