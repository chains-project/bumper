Here's a possible patch for the client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder builder = org.pitest.classinfo.ClassInfo.forName(data.getMutatedClass());
    coverage.accept(new org.pitest.coverage.CoverageVisitor() {
        @Override
        public void visit(org.pitest.classinfo.ClassInfo classInfo, byte[] classBytes, long classAddress) {
            if (classInfo.getName().equals(data.getMutatedClass())) {
                builder = builder.withCoverage(classInfo, classBytes, classAddress);
            }
        }
    });
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), builder.build());
}
```

This patch uses the new `getClassInfo` method added in `ClassInfoVisitor` to build the `ClassInfo` object for the mutated class. It then uses a `CoverageVisitor` to iterate over the coverage data and update the `ClassInfoBuilder` with the coverage information for the mutated class. Finally, it creates the `MutationTestSummaryData` object using the updated `ClassInfo` object.