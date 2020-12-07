-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 07, 2020 at 01:44 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `foodstore`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add cart', 7, 'add_cart'),
(26, 'Can change cart', 7, 'change_cart'),
(27, 'Can delete cart', 7, 'delete_cart'),
(28, 'Can view cart', 7, 'view_cart'),
(29, 'Can add category', 8, 'add_category'),
(30, 'Can change category', 8, 'change_category'),
(31, 'Can delete category', 8, 'delete_category'),
(32, 'Can view category', 8, 'view_category'),
(33, 'Can add product', 9, 'add_product'),
(34, 'Can change product', 9, 'change_product'),
(35, 'Can delete product', 9, 'delete_product'),
(36, 'Can view product', 9, 'view_product'),
(37, 'Can add review', 10, 'add_review'),
(38, 'Can change review', 10, 'change_review'),
(39, 'Can delete review', 10, 'delete_review'),
(40, 'Can view review', 10, 'view_review'),
(41, 'Can add cart item', 11, 'add_cartitem'),
(42, 'Can change cart item', 11, 'change_cartitem'),
(43, 'Can delete cart item', 11, 'delete_cartitem'),
(44, 'Can view cart item', 11, 'view_cartitem'),
(45, 'Can add blog', 12, 'add_blog'),
(46, 'Can change blog', 12, 'change_blog'),
(47, 'Can delete blog', 12, 'delete_blog'),
(48, 'Can view blog', 12, 'view_blog'),
(49, 'Can add comment', 13, 'add_comment'),
(50, 'Can change comment', 13, 'change_comment'),
(51, 'Can delete comment', 13, 'delete_comment'),
(52, 'Can view comment', 13, 'view_comment'),
(53, 'Can add reply', 14, 'add_reply'),
(54, 'Can change reply', 14, 'change_reply'),
(55, 'Can delete reply', 14, 'delete_reply'),
(56, 'Can view reply', 14, 'view_reply');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$mhaj01ZU99Kt$1r6NVMN7srIKlAWo/J0xboCgdImJ0y2jFy6P8HaRtDM=', '2020-12-07 12:12:14.725111', 1, 'admin', '', '', 'foodstore@gmail.com', 1, 1, '2020-11-13 09:57:13.657689');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `blog_blog`
--

CREATE TABLE `blog_blog` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `title` varchar(50) NOT NULL,
  `content` longtext NOT NULL,
  `author_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `blog_comment`
--

CREATE TABLE `blog_comment` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `content` longtext NOT NULL,
  `test` varchar(20) DEFAULT NULL,
  `author_id` int(11) NOT NULL,
  `blog_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `blog_reply`
--

CREATE TABLE `blog_reply` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `content` longtext NOT NULL,
  `author_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2020-11-16 12:25:30.099800', '1', 'Trái cây', 1, '[{\"added\": {}}]', 8, 1),
(2, '2020-11-16 12:25:34.874927', '2', 'Thịt', 1, '[{\"added\": {}}]', 8, 1),
(3, '2020-11-16 12:25:56.384882', '3', 'Cá', 1, '[{\"added\": {}}]', 8, 1),
(4, '2020-11-16 12:28:57.903073', '1', 'Dưa hấu', 1, '[{\"added\": {}}]', 9, 1),
(5, '2020-11-16 12:48:30.794967', '1', 'Dưa hấu', 2, '[{\"changed\": {\"fields\": [\"Thumbnail\"]}}]', 9, 1),
(6, '2020-11-16 12:51:03.833031', '2', 'Chuối', 1, '[{\"added\": {}}]', 9, 1),
(7, '2020-11-16 12:54:59.247549', '3', 'Cá hồi', 1, '[{\"added\": {}}]', 9, 1),
(8, '2020-12-07 12:16:00.673686', '4', 'Bánh Crepes', 1, '[{\"added\": {}}]', 9, 1),
(9, '2020-12-07 12:16:58.196691', '5', 'Bánh gato sô cô la', 1, '[{\"added\": {}}]', 9, 1),
(10, '2020-12-07 12:18:09.957166', '6', 'Bánh cookies', 1, '[{\"added\": {}}]', 9, 1),
(11, '2020-12-07 12:19:00.315608', '7', 'Bánh cupcake', 1, '[{\"added\": {}}]', 9, 1),
(12, '2020-12-07 12:19:42.606974', '7', 'Bánh cupcake', 2, '[{\"changed\": {\"fields\": [\"Description\"]}}]', 9, 1),
(13, '2020-12-07 12:22:53.347884', '8', 'Bánh pancake', 1, '[{\"added\": {}}]', 9, 1),
(14, '2020-12-07 12:23:36.667204', '9', 'Bánh tiramisu', 1, '[{\"added\": {}}]', 9, 1),
(15, '2020-12-07 12:24:29.298536', '10', 'Cá ngừ', 1, '[{\"added\": {}}]', 9, 1),
(16, '2020-12-07 12:25:29.762365', '11', 'Sữa tươi', 1, '[{\"added\": {}}]', 9, 1),
(17, '2020-12-07 12:26:23.137319', '12', 'Sữa đậu nành', 1, '[{\"added\": {}}]', 9, 1),
(18, '2020-12-07 12:27:07.964883', '13', 'Sữa chua nhà làm', 1, '[{\"added\": {}}]', 9, 1),
(19, '2020-12-07 12:27:53.170411', '14', 'Cánh gà', 1, '[{\"added\": {}}]', 9, 1),
(20, '2020-12-07 12:28:22.858382', '15', 'Đùi gà', 1, '[{\"added\": {}}]', 9, 1),
(21, '2020-12-07 12:28:55.058689', '16', 'Lõi bò', 1, '[{\"added\": {}}]', 9, 1),
(22, '2020-12-07 12:29:24.353391', '17', 'Thịt ba chỉ', 1, '[{\"added\": {}}]', 9, 1),
(23, '2020-12-07 12:30:05.370140', '18', 'Thịt hun khói', 1, '[{\"added\": {}}]', 9, 1),
(24, '2020-12-07 12:30:54.618151', '19', 'Xúc xích', 1, '[{\"added\": {}}]', 9, 1),
(25, '2020-12-07 12:31:55.145942', '20', 'Đào tiên', 1, '[{\"added\": {}}]', 9, 1),
(26, '2020-12-07 12:32:53.706843', '21', 'Kiwi', 1, '[{\"added\": {}}]', 9, 1),
(27, '2020-12-07 12:33:29.681365', '22', 'Quả Lê', 1, '[{\"added\": {}}]', 9, 1),
(28, '2020-12-07 12:34:03.065515', '23', 'Măng cụt', 1, '[{\"added\": {}}]', 9, 1),
(29, '2020-12-07 12:34:41.648920', '24', 'Táo', 1, '[{\"added\": {}}]', 9, 1),
(30, '2020-12-07 12:35:43.609908', '25', 'Trứng gà', 1, '[{\"added\": {}}]', 9, 1),
(31, '2020-12-07 12:36:15.112827', '26', 'Trứng vịt', 1, '[{\"added\": {}}]', 9, 1),
(32, '2020-12-07 12:37:11.665690', '27', 'Trứng cá', 1, '[{\"added\": {}}]', 9, 1),
(33, '2020-12-07 12:39:03.816822', '28', 'Thịt bò', 1, '[{\"added\": {}}]', 9, 1),
(34, '2020-12-07 12:39:49.713259', '29', 'Ức gà', 1, '[{\"added\": {}}]', 9, 1),
(35, '2020-12-07 12:41:22.802309', '30', 'Cam', 1, '[{\"added\": {}}]', 9, 1),
(36, '2020-12-07 12:41:53.192369', '31', 'Xoài', 1, '[{\"added\": {}}]', 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(12, 'blog', 'blog'),
(13, 'blog', 'comment'),
(14, 'blog', 'reply'),
(5, 'contenttypes', 'contenttype'),
(7, 'foodstore', 'cart'),
(11, 'foodstore', 'cartitem'),
(8, 'foodstore', 'category'),
(9, 'foodstore', 'product'),
(10, 'foodstore', 'review'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-11-13 09:56:32.718637'),
(2, 'auth', '0001_initial', '2020-11-13 09:56:32.981018'),
(3, 'admin', '0001_initial', '2020-11-13 09:56:33.614759'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-11-13 09:56:33.752396'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-11-13 09:56:33.759391'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-11-13 09:56:33.849137'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-11-13 09:56:33.922054'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-11-13 09:56:33.949981'),
(9, 'auth', '0004_alter_user_username_opts', '2020-11-13 09:56:33.956961'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-11-13 09:56:34.025779'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-11-13 09:56:34.028769'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-11-13 09:56:34.035750'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-11-13 09:56:34.050711'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-11-13 09:56:34.070657'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-11-13 09:56:34.103570'),
(16, 'auth', '0011_update_proxy_permissions', '2020-11-13 09:56:34.110551'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2020-11-13 09:56:34.125512'),
(18, 'foodstore', '0001_initial', '2020-11-13 09:56:34.293232'),
(19, 'foodstore', '0002_auto_20201111_0855', '2020-11-13 09:56:34.818279'),
(20, 'foodstore', '0003_auto_20201111_0859', '2020-11-13 09:56:34.825260'),
(21, 'foodstore', '0004_auto_20201111_0901', '2020-11-13 09:56:34.907041'),
(22, 'foodstore', '0005_auto_20201111_0905', '2020-11-13 09:56:34.921004'),
(23, 'foodstore', '0006_auto_20201113_0258', '2020-11-13 09:56:34.944940'),
(24, 'sessions', '0001_initial', '2020-11-13 09:56:34.985970'),
(25, 'blog', '0001_initial', '2020-11-16 12:23:54.859924'),
(26, 'foodstore', '0007_auto_20201113_1006', '2020-11-16 12:23:55.523704');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('3dqn7gl8nxdakf2yaurj5nz2d2sledtp', '.eJxVjMsOwiAURP-FtSGXhzxcuu83kMsFpWogKe3K-O_SpAtdTTJzzrxZwG0tYet5CXNiFybY6beLSM9c9yE9sN4bp1bXZY58R_ixdj61lF_Xg_07KNjLsFF5lf3NghlhhEZUKMFHawyeLTohNYD0AImEJkGatHMCnE_eDSmyzxe6XDZ8:1kdVqf:gAvHJqq0y21A7f0PNcyGFoNNW37cXrRd8O81tp1l9gM', '2020-11-27 09:58:29.151435'),
('n598v8gshwayz2nsdfyuc1k8vno3rqh0', '.eJxVjMsOwiAURP-FtSGXhzxcuu83kMsFpWogKe3K-O_SpAtdTTJzzrxZwG0tYet5CXNiFybY6beLSM9c9yE9sN4bp1bXZY58R_ixdj61lF_Xg_07KNjLsFF5lf3NghlhhEZUKMFHawyeLTohNYD0AImEJkGatHMCnE_eDSmyzxe6XDZ8:1kmFNG:NGfYDdfVDtzHWp3hDI8EMF2qighsYWkHYnU3Af5Rh7E', '2020-12-21 12:12:14.727105');

-- --------------------------------------------------------

--
-- Table structure for table `foodstore_cart`
--

CREATE TABLE `foodstore_cart` (
  `id` int(11) NOT NULL,
  `date_created` date NOT NULL,
  `coupon` double NOT NULL,
  `total_price` double NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `foodstore_cartitem`
--

CREATE TABLE `foodstore_cartitem` (
  `id` int(11) NOT NULL,
  `quantity` int(10) UNSIGNED NOT NULL CHECK (`quantity` >= 0),
  `price` double NOT NULL,
  `cart_id` int(11) NOT NULL,
  `products_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `foodstore_category`
--

CREATE TABLE `foodstore_category` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `slug` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `foodstore_category`
--

INSERT INTO `foodstore_category` (`id`, `name`, `slug`) VALUES
(1, 'Trái cây', 'trai-cay'),
(2, 'Thịt', 'thit'),
(3, 'Cá', 'ca'),
(6, 'Sữa', 'sua'),
(8, 'Trứng', 'trung'),
(9, 'Bánh', 'banh');

-- --------------------------------------------------------

--
-- Table structure for table `foodstore_product`
--

CREATE TABLE `foodstore_product` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `price` double NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `description` longtext NOT NULL,
  `status` int(11) NOT NULL,
  `ship` varchar(50) NOT NULL,
  `amount` double NOT NULL,
  `date_created` date NOT NULL,
  `category_id` int(11) NOT NULL,
  `unit` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `foodstore_product`
--

INSERT INTO `foodstore_product` (`id`, `name`, `price`, `thumbnail`, `description`, `status`, `ship`, `amount`, `date_created`, `category_id`, `unit`) VALUES
(1, 'Dưa hấu', 10, 'uploads/product_thumbnails/2020/11/16/duahau.jpg', 'Dưa hấu thần, ăn vào sẽ trường sinh bất lão.', 0, '10000 năm', 0, '2020-11-16', 1, 'kg'),
(2, 'Chuối', 7, 'uploads/product_thumbnails/2020/11/16/chuoi.jpg', 'Chuối đà lạt.', 0, '1 ngày', 2, '2020-11-16', 1, 'nải'),
(3, 'Cá hồi', 30, 'uploads/product_thumbnails/2020/11/16/cá_hồi.jpg', 'Cá atlantis', 1, '2 giờ', 2, '2020-11-16', 3, 'kg'),
(4, 'Bánh Crepes', 50000, 'uploads/product_thumbnails/2020/12/07/banhcrepes.jpg', 'Bánh kếp nhập khẩu', 1, '1 giờ', 10, '2020-12-07', 9, 'cái'),
(5, 'Bánh gato sô cô la', 100000, 'uploads/product_thumbnails/2020/12/07/banhsocola.jpg', 'Bánh sinh nhật sô cô la', 1, '1 giờ', 5, '2020-12-07', 9, 'cái'),
(6, 'Bánh cookies', 30000, 'uploads/product_thumbnails/2020/12/07/cookies.jpg', 'bánh cookies cookies', 1, '1 giờ', 30, '2020-12-07', 9, 'hộp'),
(7, 'Bánh cupcake', 10000, 'uploads/product_thumbnails/2020/12/07/cupcake.jpg', 'Bánh Cupcake hay còn gọi là Muffin.', 1, '1 giờ', 50, '2020-12-07', 9, 'cái'),
(8, 'Bánh pancake', 40000, 'uploads/product_thumbnails/2020/12/07/pancake.jpg', 'Bánh ngon dưới mật ong', 1, '1 giờ', 100, '2020-12-07', 9, 'cái'),
(9, 'Bánh tiramisu', 60000, 'uploads/product_thumbnails/2020/12/07/tiramisu.jpg', 'Bánh ngọt của Nhật , ăn siêu ngon.', 1, '1 giờ', 60, '2020-12-07', 9, 'cái'),
(10, 'Cá ngừ', 100000, 'uploads/product_thumbnails/2020/12/07/cangu.jpg', 'Cá ngừ đại dương.', 1, '1 giờ', 100, '2020-12-07', 3, 'kg'),
(11, 'Sữa tươi', 47000, 'uploads/product_thumbnails/2020/12/07/sua.jpg', 'Bữa Sò', 1, '1 giờ', 1000, '2020-12-07', 6, 'chai'),
(12, 'Sữa đậu nành', 30000, 'uploads/product_thumbnails/2020/12/07/suadaunanh.jpg', 'Sữa đậu nành dành cho người quan tâm đến vóc dáng.', 1, '1 giờ', 100, '2020-12-07', 6, 'chai'),
(13, 'Sữa chua nhà làm', 15000, 'uploads/product_thumbnails/2020/12/07/suachuanhalam.jpg', 'Sữa chua nhà tự làm. 15.000VNĐ/1 hộp', 1, '1 giờ', 100, '2020-12-07', 6, 'hộp'),
(14, 'Cánh gà', 66000, 'uploads/product_thumbnails/2020/12/07/canhga.jpg', 'Chicken wings.', 1, '1 giờ', 34, '2020-12-07', 2, 'kg'),
(15, 'Đùi gà', 76000, 'uploads/product_thumbnails/2020/12/07/duiga.jpg', 'gà đùi', 1, '1 giờ', 324, '2020-12-07', 2, 'kg'),
(16, 'Lõi bò', 120000, 'uploads/product_thumbnails/2020/12/07/loibo.jpg', 'Phần ngon nhất của 1 con bò.', 1, '1 giờ', 353, '2020-12-07', 2, 'kg'),
(17, 'Thịt ba chỉ', 35000, 'uploads/product_thumbnails/2020/12/07/thit-ba-chi.jpg', 'Ba chỉ thơm ngon.', 1, '1 giờ', 234, '2020-12-07', 2, 'kg'),
(18, 'Thịt hun khói', 40000, 'uploads/product_thumbnails/2020/12/07/thithunkhoi.jpg', 'khói hun thịt.', 1, '1 giờ', 345, '2020-12-07', 2, 'kg'),
(19, 'Xúc xích', 26000, 'uploads/product_thumbnails/2020/12/07/xucxich.jpg', 'Xúc xích cũng là thịt.', 1, '1 giờ', 45, '2020-12-07', 2, 'kg'),
(20, 'Đào tiên', 999999, 'uploads/product_thumbnails/2020/12/07/dao.jpg', 'Đào tiên trên thiên đình. Ăn vào trường sinh bất lão.', 1, '10000 năm', 1, '2020-12-07', 1, 'kg'),
(21, 'Kiwi', 20000, 'uploads/product_thumbnails/2020/12/07/kiwi.jpg', 'trái cây đến từ phương Tây.', 1, '2 giờ', 5463, '2020-12-07', 1, 'kg'),
(22, 'Quả Lê', 16000, 'uploads/product_thumbnails/2020/12/07/le.jpg', 'đây là quả lê.', 1, '1 giờ', 24, '2020-12-07', 1, 'kg'),
(23, 'Măng cụt', 34000, 'uploads/product_thumbnails/2020/12/07/mang-cut.jpg', 'Quả măng bị cụt.', 1, '1 giờ', 345, '2020-12-07', 1, 'kg'),
(24, 'Táo', 3453344, 'uploads/product_thumbnails/2020/12/07/tao.jpg', 'Táo độc của mụ phù thủy.', 1, '1 ngày', 1, '2020-12-07', 1, 'kg'),
(25, 'Trứng gà', 3000, 'uploads/product_thumbnails/2020/12/07/trungga.jpg', 'Con gà có trước hay quả trứng có trước?', 1, '1 giờ', 33, '2020-12-07', 8, 'quả'),
(26, 'Trứng vịt', 3000, 'uploads/product_thumbnails/2020/12/07/trungvit.jpg', 'Con vịt có trước hay quả trứng có trước?', 1, '1 giờ', 345, '2020-12-07', 8, 'quả'),
(27, 'Trứng cá', 33000, 'uploads/product_thumbnails/2020/12/07/trungcahoi.jpg', 'Trứng của con cá hồi. ăn để tăng DHA.', 1, '1 giờ', 23, '2020-12-07', 8, 'g'),
(28, 'Thịt bò', 80000, 'uploads/product_thumbnails/2020/12/07/thitbo.jpg', 'Thịt bò ngon và mềm.', 1, '1 giờ', 34534, '2020-12-07', 2, 'kg'),
(29, 'Ức gà', 22000, 'uploads/product_thumbnails/2020/12/07/ucga.jpg', 'Giàu protein.', 1, '1 giờ', 54, '2020-12-07', 2, 'kg'),
(30, 'Cam', 20000, 'uploads/product_thumbnails/2020/12/07/cam.jpg', 'cam vì nó màu cam', 1, '1 giờ', 345, '2020-12-07', 1, 'kg'),
(31, 'Xoài', 17000, 'uploads/product_thumbnails/2020/12/07/xoai.jpg', 'Xoài ăn ngọt.', 1, '1 giờ', 435, '2020-12-07', 1, 'kg');

-- --------------------------------------------------------

--
-- Table structure for table `foodstore_review`
--

CREATE TABLE `foodstore_review` (
  `id` int(11) NOT NULL,
  `stars` int(11) NOT NULL,
  `comment` longtext NOT NULL,
  `date_created` date NOT NULL,
  `product_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `blog_blog`
--
ALTER TABLE `blog_blog`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD KEY `blog_blog_author_id_8791af69_fk_auth_user_id` (`author_id`);

--
-- Indexes for table `blog_comment`
--
ALTER TABLE `blog_comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `blog_comment_author_id_4f11e2e0_fk_auth_user_id` (`author_id`),
  ADD KEY `blog_comment_blog_id_c664fb0d_fk_blog_blog_id` (`blog_id`);

--
-- Indexes for table `blog_reply`
--
ALTER TABLE `blog_reply`
  ADD PRIMARY KEY (`id`),
  ADD KEY `blog_reply_author_id_7641dac7_fk_auth_user_id` (`author_id`),
  ADD KEY `blog_reply_comment_id_be7970f5_fk_blog_comment_id` (`comment_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `foodstore_cart`
--
ALTER TABLE `foodstore_cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `foodstore_cart_user_id_919fe6a4_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `foodstore_cartitem`
--
ALTER TABLE `foodstore_cartitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `foodstore_cartitem_cart_id_c5ee8d68_fk_foodstore_cart_id` (`cart_id`),
  ADD KEY `foodstore_cartitem_products_id_60abd493_fk_foodstore_product_id` (`products_id`);

--
-- Indexes for table `foodstore_category`
--
ALTER TABLE `foodstore_category`
  ADD PRIMARY KEY (`id`),
  ADD KEY `foodstore_category_slug_35326df7` (`slug`);

--
-- Indexes for table `foodstore_product`
--
ALTER TABLE `foodstore_product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `foodstore_product_category_id_49e3988a_fk_foodstore_category_id` (`category_id`);

--
-- Indexes for table `foodstore_review`
--
ALTER TABLE `foodstore_review`
  ADD PRIMARY KEY (`id`),
  ADD KEY `foodstore_review_product_id_f830c360_fk_foodstore_product_id` (`product_id`),
  ADD KEY `foodstore_review_user_id_98da7ec7_fk_auth_user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `blog_blog`
--
ALTER TABLE `blog_blog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `blog_comment`
--
ALTER TABLE `blog_comment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `blog_reply`
--
ALTER TABLE `blog_reply`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `foodstore_cart`
--
ALTER TABLE `foodstore_cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `foodstore_cartitem`
--
ALTER TABLE `foodstore_cartitem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `foodstore_category`
--
ALTER TABLE `foodstore_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `foodstore_product`
--
ALTER TABLE `foodstore_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `foodstore_review`
--
ALTER TABLE `foodstore_review`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `blog_blog`
--
ALTER TABLE `blog_blog`
  ADD CONSTRAINT `blog_blog_author_id_8791af69_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `blog_comment`
--
ALTER TABLE `blog_comment`
  ADD CONSTRAINT `blog_comment_author_id_4f11e2e0_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `blog_comment_blog_id_c664fb0d_fk_blog_blog_id` FOREIGN KEY (`blog_id`) REFERENCES `blog_blog` (`id`);

--
-- Constraints for table `blog_reply`
--
ALTER TABLE `blog_reply`
  ADD CONSTRAINT `blog_reply_author_id_7641dac7_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `blog_reply_comment_id_be7970f5_fk_blog_comment_id` FOREIGN KEY (`comment_id`) REFERENCES `blog_comment` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `foodstore_cart`
--
ALTER TABLE `foodstore_cart`
  ADD CONSTRAINT `foodstore_cart_user_id_919fe6a4_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `foodstore_cartitem`
--
ALTER TABLE `foodstore_cartitem`
  ADD CONSTRAINT `foodstore_cartitem_cart_id_c5ee8d68_fk_foodstore_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `foodstore_cart` (`id`),
  ADD CONSTRAINT `foodstore_cartitem_products_id_60abd493_fk_foodstore_product_id` FOREIGN KEY (`products_id`) REFERENCES `foodstore_product` (`id`);

--
-- Constraints for table `foodstore_product`
--
ALTER TABLE `foodstore_product`
  ADD CONSTRAINT `foodstore_product_category_id_49e3988a_fk_foodstore_category_id` FOREIGN KEY (`category_id`) REFERENCES `foodstore_category` (`id`);

--
-- Constraints for table `foodstore_review`
--
ALTER TABLE `foodstore_review`
  ADD CONSTRAINT `foodstore_review_product_id_f830c360_fk_foodstore_product_id` FOREIGN KEY (`product_id`) REFERENCES `foodstore_product` (`id`),
  ADD CONSTRAINT `foodstore_review_user_id_98da7ec7_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
