Here's the fixed version of the method:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder builder = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass(), new byte[0], 0);
    org.pitest.classinfo.ClassInfo classInfo = builder.build();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

In this version, I used the new `getClassInfo` method from `ClassInfoVisitor` to build a `ClassInfo` object from the mutated class name. Then, I used this object to create the `MutationTestSummaryData` object.