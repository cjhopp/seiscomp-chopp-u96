/********************************************************************************
** Form generated from reading UI file 'origindialog.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ORIGINDIALOG_H
#define UI_ORIGINDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDateTimeEdit>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_OriginDialog
{
public:
    QVBoxLayout *vboxLayout;
    QGroupBox *groupBox;
    QGridLayout *gridLayout;
    QLabel *label_2;
    QDoubleSpinBox *depthDoubleSpinBox;
    QLabel *lonLabel;
    QDoubleSpinBox *lonDoubleSpinBox;
    QLabel *latLabel;
    QLabel *label;
    QDoubleSpinBox *latDoubleSpinBox;
    QDateTimeEdit *dateTimeEdit;
    QGroupBox *advancedGB;
    QGridLayout *gridLayout1;
    QDoubleSpinBox *magSB;
    QLabel *magTypeLabel;
    QComboBox *magTypeCB;
    QLabel *magLabel;
    QLabel *phaseCountLabel;
    QDoubleSpinBox *phaseCountSB;
    QSpacerItem *spacerItem;
    QHBoxLayout *hboxLayout;
    QSpacerItem *spacerItem1;
    QPushButton *sendButton;
    QPushButton *cancelButton;

    void setupUi(QDialog *OriginDialog)
    {
        if (OriginDialog->objectName().isEmpty())
            OriginDialog->setObjectName(QString::fromUtf8("OriginDialog"));
        OriginDialog->resize(238, 122);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Minimum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(OriginDialog->sizePolicy().hasHeightForWidth());
        OriginDialog->setSizePolicy(sizePolicy);
        vboxLayout = new QVBoxLayout(OriginDialog);
#ifndef Q_OS_MAC
        vboxLayout->setSpacing(6);
#endif
#ifndef Q_OS_MAC
        vboxLayout->setContentsMargins(9, 9, 9, 9);
#endif
        vboxLayout->setObjectName(QString::fromUtf8("vboxLayout"));
        groupBox = new QGroupBox(OriginDialog);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout = new QGridLayout(groupBox);
#ifndef Q_OS_MAC
        gridLayout->setSpacing(6);
#endif
#ifndef Q_OS_MAC
        gridLayout->setContentsMargins(9, 9, 9, 9);
#endif
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_2 = new QLabel(groupBox);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 3, 0, 1, 1);

        depthDoubleSpinBox = new QDoubleSpinBox(groupBox);
        depthDoubleSpinBox->setObjectName(QString::fromUtf8("depthDoubleSpinBox"));
        depthDoubleSpinBox->setAlignment(Qt::AlignRight);
        depthDoubleSpinBox->setDecimals(3);
        depthDoubleSpinBox->setMaximum(1000.000000000000000);
        depthDoubleSpinBox->setMinimum(-100.000000000000000);
        depthDoubleSpinBox->setSingleStep(10.000000000000000);
        depthDoubleSpinBox->setValue(10.000000000000000);

        gridLayout->addWidget(depthDoubleSpinBox, 3, 1, 1, 1);

        lonLabel = new QLabel(groupBox);
        lonLabel->setObjectName(QString::fromUtf8("lonLabel"));

        gridLayout->addWidget(lonLabel, 2, 0, 1, 1);

        lonDoubleSpinBox = new QDoubleSpinBox(groupBox);
        lonDoubleSpinBox->setObjectName(QString::fromUtf8("lonDoubleSpinBox"));
        lonDoubleSpinBox->setMinimumSize(QSize(130, 0));
        lonDoubleSpinBox->setAlignment(Qt::AlignRight);
        lonDoubleSpinBox->setDecimals(4);
        lonDoubleSpinBox->setMaximum(180.000000000000000);
        lonDoubleSpinBox->setMinimum(-180.000000000000000);
        lonDoubleSpinBox->setValue(0.000000000000000);

        gridLayout->addWidget(lonDoubleSpinBox, 2, 1, 1, 1);

        latLabel = new QLabel(groupBox);
        latLabel->setObjectName(QString::fromUtf8("latLabel"));

        gridLayout->addWidget(latLabel, 1, 0, 1, 1);

        label = new QLabel(groupBox);
        label->setObjectName(QString::fromUtf8("label"));
        QSizePolicy sizePolicy1(QSizePolicy::Maximum, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy1);

        gridLayout->addWidget(label, 0, 0, 1, 1);

        latDoubleSpinBox = new QDoubleSpinBox(groupBox);
        latDoubleSpinBox->setObjectName(QString::fromUtf8("latDoubleSpinBox"));
        latDoubleSpinBox->setMinimumSize(QSize(130, 0));
        latDoubleSpinBox->setAlignment(Qt::AlignRight);
        latDoubleSpinBox->setDecimals(4);
        latDoubleSpinBox->setMaximum(90.000000000000000);
        latDoubleSpinBox->setMinimum(-90.000000000000000);

        gridLayout->addWidget(latDoubleSpinBox, 1, 1, 1, 1);

        dateTimeEdit = new QDateTimeEdit(groupBox);
        dateTimeEdit->setObjectName(QString::fromUtf8("dateTimeEdit"));
        dateTimeEdit->setAlignment(Qt::AlignRight);
        dateTimeEdit->setCurrentSection(QDateTimeEdit::YearSection);

        gridLayout->addWidget(dateTimeEdit, 0, 1, 1, 1);


        vboxLayout->addWidget(groupBox);

        advancedGB = new QGroupBox(OriginDialog);
        advancedGB->setObjectName(QString::fromUtf8("advancedGB"));
        advancedGB->setEnabled(true);
        advancedGB->setCheckable(true);
        advancedGB->setChecked(false);
        gridLayout1 = new QGridLayout(advancedGB);
#ifndef Q_OS_MAC
        gridLayout1->setSpacing(6);
#endif
#ifndef Q_OS_MAC
        gridLayout1->setContentsMargins(9, 9, 9, 9);
#endif
        gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
        magSB = new QDoubleSpinBox(advancedGB);
        magSB->setObjectName(QString::fromUtf8("magSB"));
        magSB->setAlignment(Qt::AlignRight);
        magSB->setMaximum(10.000000000000000);
        magSB->setSingleStep(0.200000000000000);
        magSB->setValue(5.000000000000000);

        gridLayout1->addWidget(magSB, 1, 1, 1, 1);

        magTypeLabel = new QLabel(advancedGB);
        magTypeLabel->setObjectName(QString::fromUtf8("magTypeLabel"));
        sizePolicy1.setHeightForWidth(magTypeLabel->sizePolicy().hasHeightForWidth());
        magTypeLabel->setSizePolicy(sizePolicy1);

        gridLayout1->addWidget(magTypeLabel, 2, 0, 1, 1);

        magTypeCB = new QComboBox(advancedGB);
        magTypeCB->setObjectName(QString::fromUtf8("magTypeCB"));
        magTypeCB->setEditable(true);
        magTypeCB->setMaxVisibleItems(30);

        gridLayout1->addWidget(magTypeCB, 2, 1, 1, 1);

        magLabel = new QLabel(advancedGB);
        magLabel->setObjectName(QString::fromUtf8("magLabel"));
        sizePolicy1.setHeightForWidth(magLabel->sizePolicy().hasHeightForWidth());
        magLabel->setSizePolicy(sizePolicy1);

        gridLayout1->addWidget(magLabel, 1, 0, 1, 1);

        phaseCountLabel = new QLabel(advancedGB);
        phaseCountLabel->setObjectName(QString::fromUtf8("phaseCountLabel"));
        sizePolicy1.setHeightForWidth(phaseCountLabel->sizePolicy().hasHeightForWidth());
        phaseCountLabel->setSizePolicy(sizePolicy1);

        gridLayout1->addWidget(phaseCountLabel, 0, 0, 1, 1);

        phaseCountSB = new QDoubleSpinBox(advancedGB);
        phaseCountSB->setObjectName(QString::fromUtf8("phaseCountSB"));
        phaseCountSB->setAlignment(Qt::AlignRight);
        phaseCountSB->setDecimals(0);
        phaseCountSB->setMaximum(10000.000000000000000);
        phaseCountSB->setValue(10.000000000000000);

        gridLayout1->addWidget(phaseCountSB, 0, 1, 1, 1);


        vboxLayout->addWidget(advancedGB);

        spacerItem = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        vboxLayout->addItem(spacerItem);

        hboxLayout = new QHBoxLayout();
#ifndef Q_OS_MAC
        hboxLayout->setSpacing(6);
#endif
        hboxLayout->setContentsMargins(0, 0, 0, 0);
        hboxLayout->setObjectName(QString::fromUtf8("hboxLayout"));
        spacerItem1 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        hboxLayout->addItem(spacerItem1);

        sendButton = new QPushButton(OriginDialog);
        sendButton->setObjectName(QString::fromUtf8("sendButton"));
        QPalette palette;
        palette.setColor(QPalette::Active, QPalette::WindowText, QColor(0, 0, 0));
        palette.setColor(QPalette::Active, QPalette::Button, QColor(221, 223, 228));
        palette.setColor(QPalette::Active, QPalette::Light, QColor(255, 255, 255));
        palette.setColor(QPalette::Active, QPalette::Midlight, QColor(255, 255, 255));
        palette.setColor(QPalette::Active, QPalette::Dark, QColor(85, 85, 85));
        palette.setColor(QPalette::Active, QPalette::Mid, QColor(199, 199, 199));
        palette.setColor(QPalette::Active, QPalette::Text, QColor(0, 0, 0));
        palette.setColor(QPalette::Active, QPalette::BrightText, QColor(255, 255, 255));
        palette.setColor(QPalette::Active, QPalette::ButtonText, QColor(0, 0, 0));
        palette.setColor(QPalette::Active, QPalette::Base, QColor(255, 255, 255));
        palette.setColor(QPalette::Active, QPalette::Window, QColor(239, 239, 239));
        palette.setColor(QPalette::Active, QPalette::Shadow, QColor(0, 0, 0));
        palette.setColor(QPalette::Active, QPalette::Highlight, QColor(103, 141, 178));
        palette.setColor(QPalette::Active, QPalette::HighlightedText, QColor(255, 255, 255));
        palette.setColor(QPalette::Active, QPalette::Link, QColor(0, 0, 238));
        palette.setColor(QPalette::Active, QPalette::LinkVisited, QColor(82, 24, 139));
        palette.setColor(QPalette::Active, QPalette::AlternateBase, QColor(232, 232, 232));
        palette.setColor(QPalette::Inactive, QPalette::WindowText, QColor(0, 0, 0));
        palette.setColor(QPalette::Inactive, QPalette::Button, QColor(221, 223, 228));
        palette.setColor(QPalette::Inactive, QPalette::Light, QColor(255, 255, 255));
        palette.setColor(QPalette::Inactive, QPalette::Midlight, QColor(255, 255, 255));
        palette.setColor(QPalette::Inactive, QPalette::Dark, QColor(85, 85, 85));
        palette.setColor(QPalette::Inactive, QPalette::Mid, QColor(199, 199, 199));
        palette.setColor(QPalette::Inactive, QPalette::Text, QColor(0, 0, 0));
        palette.setColor(QPalette::Inactive, QPalette::BrightText, QColor(255, 255, 255));
        palette.setColor(QPalette::Inactive, QPalette::ButtonText, QColor(0, 0, 0));
        palette.setColor(QPalette::Inactive, QPalette::Base, QColor(255, 255, 255));
        palette.setColor(QPalette::Inactive, QPalette::Window, QColor(239, 239, 239));
        palette.setColor(QPalette::Inactive, QPalette::Shadow, QColor(0, 0, 0));
        palette.setColor(QPalette::Inactive, QPalette::Highlight, QColor(103, 141, 178));
        palette.setColor(QPalette::Inactive, QPalette::HighlightedText, QColor(255, 255, 255));
        palette.setColor(QPalette::Inactive, QPalette::Link, QColor(0, 0, 238));
        palette.setColor(QPalette::Inactive, QPalette::LinkVisited, QColor(82, 24, 139));
        palette.setColor(QPalette::Inactive, QPalette::AlternateBase, QColor(232, 232, 232));
        palette.setColor(QPalette::Disabled, QPalette::WindowText, QColor(128, 128, 128));
        palette.setColor(QPalette::Disabled, QPalette::Button, QColor(221, 223, 228));
        palette.setColor(QPalette::Disabled, QPalette::Light, QColor(255, 255, 255));
        palette.setColor(QPalette::Disabled, QPalette::Midlight, QColor(255, 255, 255));
        palette.setColor(QPalette::Disabled, QPalette::Dark, QColor(85, 85, 85));
        palette.setColor(QPalette::Disabled, QPalette::Mid, QColor(199, 199, 199));
        palette.setColor(QPalette::Disabled, QPalette::Text, QColor(199, 199, 199));
        palette.setColor(QPalette::Disabled, QPalette::BrightText, QColor(255, 255, 255));
        palette.setColor(QPalette::Disabled, QPalette::ButtonText, QColor(128, 128, 128));
        palette.setColor(QPalette::Disabled, QPalette::Base, QColor(239, 239, 239));
        palette.setColor(QPalette::Disabled, QPalette::Window, QColor(239, 239, 239));
        palette.setColor(QPalette::Disabled, QPalette::Shadow, QColor(0, 0, 0));
        palette.setColor(QPalette::Disabled, QPalette::Highlight, QColor(86, 117, 148));
        palette.setColor(QPalette::Disabled, QPalette::HighlightedText, QColor(255, 255, 255));
        palette.setColor(QPalette::Disabled, QPalette::Link, QColor(0, 0, 238));
        palette.setColor(QPalette::Disabled, QPalette::LinkVisited, QColor(82, 24, 139));
        palette.setColor(QPalette::Disabled, QPalette::AlternateBase, QColor(232, 232, 232));
        sendButton->setPalette(palette);

        hboxLayout->addWidget(sendButton);

        cancelButton = new QPushButton(OriginDialog);
        cancelButton->setObjectName(QString::fromUtf8("cancelButton"));

        hboxLayout->addWidget(cancelButton);


        vboxLayout->addLayout(hboxLayout);

        QWidget::setTabOrder(dateTimeEdit, latDoubleSpinBox);
        QWidget::setTabOrder(latDoubleSpinBox, lonDoubleSpinBox);
        QWidget::setTabOrder(lonDoubleSpinBox, depthDoubleSpinBox);
        QWidget::setTabOrder(depthDoubleSpinBox, sendButton);
        QWidget::setTabOrder(sendButton, cancelButton);

        retranslateUi(OriginDialog);
        QObject::connect(sendButton, SIGNAL(clicked()), OriginDialog, SLOT(accept()));
        QObject::connect(cancelButton, SIGNAL(clicked()), OriginDialog, SLOT(reject()));

        QMetaObject::connectSlotsByName(OriginDialog);
    } // setupUi

    void retranslateUi(QDialog *OriginDialog)
    {
        OriginDialog->setWindowTitle(QCoreApplication::translate("OriginDialog", "Artificial Origin", nullptr));
        groupBox->setTitle(QCoreApplication::translate("OriginDialog", "Origin", nullptr));
        label_2->setText(QCoreApplication::translate("OriginDialog", "Depth:", nullptr));
        depthDoubleSpinBox->setSuffix(QCoreApplication::translate("OriginDialog", " km", nullptr));
        lonLabel->setText(QCoreApplication::translate("OriginDialog", "Lon:", nullptr));
        lonDoubleSpinBox->setSuffix(QCoreApplication::translate("OriginDialog", " deg", nullptr));
        latLabel->setText(QCoreApplication::translate("OriginDialog", "Lat:", nullptr));
        label->setText(QCoreApplication::translate("OriginDialog", "Time:", nullptr));
        latDoubleSpinBox->setSuffix(QCoreApplication::translate("OriginDialog", " deg", nullptr));
        dateTimeEdit->setDisplayFormat(QCoreApplication::translate("OriginDialog", "yyyy-MM-dd hh:mm:ss", nullptr));
        advancedGB->setTitle(QCoreApplication::translate("OriginDialog", "Advanced", nullptr));
        magTypeLabel->setText(QCoreApplication::translate("OriginDialog", "Magnitude Type", nullptr));
        magLabel->setText(QCoreApplication::translate("OriginDialog", "Magnitude", nullptr));
        phaseCountLabel->setText(QCoreApplication::translate("OriginDialog", "PhaseCount", nullptr));
        sendButton->setText(QCoreApplication::translate("OriginDialog", "Create", nullptr));
        cancelButton->setText(QCoreApplication::translate("OriginDialog", "Cancel", nullptr));
    } // retranslateUi

};

namespace Ui {
    class OriginDialog: public Ui_OriginDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ORIGINDIALOG_H
