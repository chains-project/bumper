Here's a fixed version of the `createSummaryData` method that should work with the updated library:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass(), new byte[0], 0);
    coverage.accept(classInfoBuilder);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder.build());
}
```

This version of the method creates a `ClassInfoBuilder` using the new `getClassInfo` method added to `ClassInfoVisitor`, then uses the `accept` method of the `CoverageDatabase` to populate the builder with coverage information. Finally, the `build` method is called on the `ClassInfoBuilder` to create a `ClassInfo` object that can be passed to the `MutationTestSummaryData` constructor.

Note that this version of the method assumes that the `data.getMutatedClass()` method returns a single `ClassName` object. If it returns a collection of `ClassName` objects, the `getClassInfo` method would need to be called in a loop to handle each class separately.