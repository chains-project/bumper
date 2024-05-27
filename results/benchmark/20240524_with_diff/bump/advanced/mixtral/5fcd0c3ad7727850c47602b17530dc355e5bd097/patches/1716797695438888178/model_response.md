Here's a patch that you can apply to the `createSummaryData` method to fix the error:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(data.getMutatedClass().asString()));
}
```

The change here is to use the `asString()` method of `data.getMutatedClass()` to convert the `ClassName` object to a string, which can then be passed to `coverage.getClassInfo()` as a single-element `Set`. This works because the new library version includes a new `getClassInfo()` method that accepts a `ClassName` and a byte array.

Note that this solution assumes that the `coverage.getClassInfo()` method is able to handle a single `ClassName` as a `Set<ClassName>` argument. If not, you may need to modify the solution accordingly.