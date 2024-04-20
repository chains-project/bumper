Here's a patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder builder = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass(), new byte[0], 0);
    org.pitest.classinfo.ClassInfo classInfo = builder.build();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

This patch creates a `ClassInfo` instance by using the new `getClassInfo` method from `ClassInfoVisitor`, which takes a `ClassName`, byte array, and long as arguments. The method returns a `ClassInfoBuilder`, from which we can build a `ClassInfo` instance using the `build` method. This `ClassInfo` instance is then used in the `MutationTestSummaryData` constructor.